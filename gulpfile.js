var fs = require('fs');
var path = require('path');
var gulp = require('gulp');
var sass = require('gulp-sass');
var shell = require('gulp-shell');
var gutil = require('gulp-util');
var clean = require('gulp-clean');
var jsdom = require('jsdom');
var merge = require('merge-stream');
var rename = require('gulp-rename');
var isNumeric = require('isnumeric');
var cleanCSS = require('gulp-clean-css');
var gulpSequence = require('gulp-sequence')

/**
 * The shell command that builds a set of *.md files into an *.html file.
 */
const PANDOC_COMMAND_ARR = [
    // executable
    'pandoc',
    
    // This `undefined` item stands in place of the actual input filenames.
    // The item will be replaced by an actual list of all files, starting
    // from index.md and then containing all the modules in numeric order.
    undefined,
    
    // Output filename
    '-o', 'out/index-<%= lang %>.html',
    
    // Additional Metadata arguments
    '--metadata', 'lang:<%= lang %>', // The language of the document
    
    // More options
    '-t', 'html5',                 // format used to write the output
    '--smart',                     // smart quotes and hyphens
    '--template', 'template.html', // HTML template to use
    '--css', 'css/main.min.css',   // CSS to link to from the output
    '--highlight-style', 'tango',  // highlighting syntax for code sections
];

/**
 * The regular expression to validate modules with content
 */
const MODULE_REGEX = /^module(\d+).md$/;

/**
 * Return an array with the input files in a given language directory,
 * corresponding to the index.md and module*.md files, whereis any digit-only
 * string. The array contains the index.md in the first position (if one such
 * file exists) and the module*.md files sorted in numeric order after that.
 */
function getInputFiles(lang) {
    // Get all the files in the directory. Then assign to each a numeric value
    // for subsequent sorting purposes: `index.md` gets 0; `module*.md` gets the
    // numeric value of the `*`. Then, keep the files with a numeric value;
    // the rest are not valid for our purposes.
    var files = fs
        .readdirSync(lang)
        .reduce((current, filename) => {
            var value = false;
            
            if (filename === 'index.md') {
                value = 0;
            }
            else {
                var match = MODULE_REGEX.exec(filename);
                if (match !== null) {
                    value = parseInt(match[1])
                }
            }
            
            // Only update the current array if a valid file has been found
            if (value !== false) {
                current.push({ filename, value });
            }
            
            return current;
        }, []);
    
    // Sort the files using their numeric value
    files.sort((a, b) => a.value - b.value);
    
    // Return the file names, joined with the name of the language directory
    return files.map(item => path.join(lang, item.filename));
}

/**
 * Return an array with the language directories of this project. A language
 * directory is a directory whose name is a two letter word
 */
function findLanguages() {
    return fs
        .readdirSync('.')
        .filter(item => item.length === 2 && fs.statSync(item).isDirectory());
}

/**
 * Return a gulp pipeline that builds the index.html file from the *.md files
 * of a given language directory, thus building the main site of a given
 * localization.
 */
function buildIndex(lang) {
    var command = PANDOC_COMMAND_ARR.slice();
    var files = getInputFiles(lang);
    
    // Replace the `undefined` in the command array with the actual array of
    // input file names
    var index = command.indexOf(undefined);
    
    // This next cryptic line calls command.splice with a variable number
    // of arguments, thus removing the `undefined` item from the array
    // and replacing it with each item that is contained in `files`
    Array.prototype.splice.apply(command, [index, 1].concat(files));
    
    return gulp
        .src(lang + '/*.md')
        .pipe(
            shell([ command.join(' ') ], {
                templateData: { lang }
            })
        )
        .on('end', () => {
            jsdom.env({
                file: 'out/index-' + lang + '.html',
                scripts: ['http://code.jquery.com/jquery.js'],
                done(err, window) {
                    var $ = window.$;
                    
                    // Replace '???' inside <code> elements with
                    // <span class="blank">?</span>
                    $('code').html(function() {
                        // Note that this cannot be defined with ES6's arrow
                        // functions because `this` is undefined in those
                        // constructs, rendering the function unusable
                        return $(this)
                            .html()
                            .replace(/\?\?\?/g, '<span class="blank">?</span>');
                    });

                    // `print` is a builtin in python3 but a keyworkd in python2.
                    // Let's also make this change here
                    $('span.bu').each(function() {
                        // See above for why we're not using arrow functions
                        if ($(this).text() === 'print') {
                            $(this).removeClass('bu');
                            $(this).addClass('kw');
                        }
                    });
                    
                    // Remove the extra jquery <script> element
                    $('script.jsdom').remove();
                    
                    // Write the resulting file back into its output filename
                    var newSource = $('html')[0].outerHTML;
                    fs.writeFileSync(
                        'out/index-' + lang + '.html',
                        '<!DOCTYPE html>\n' + newSource
                    );
                }
            });
        });
}

gulp.task('build', () => {
    var tasks = findLanguages().map(buildIndex);
    return merge(tasks);
});

gulp.task('sass', () => {
    var options = {
        outputStyle: 'compressed',
    };
    
    return gulp
        .src('styles/sass/*.scss')
        .pipe(sass(options).on('error', sass.logError))
        .pipe(gulp.dest('out/css'));
});

gulp.task('minify-css', () => {
    return gulp
        .src(['out/css/*.css', '!out/css/main.min.css'])
        .pipe(cleanCSS())
        .pipe(rename('main.min.css'))
        .pipe(gulp.dest('out/css'))
});

gulp.task('clean-css', () => {
    return gulp
        .src(['out/css/*.css', '!out/css/main.min.css'])
        .pipe(clean());
});

gulp.task('watch', () => {
    gulp.watch('styles/sass/*.scss', () => {
        gulpSequence('sass', 'minify-css', 'clean-css')();
    });
    gulp.watch('en/*.md', ['build-en']);
    gulp.watch('pt/*.md', ['build-pt']);
});
