var fs = require('fs');
var path = require('path');
var gulp = require('gulp');
var sass = require('gulp-sass');
var shell = require('gulp-shell');
var gutil = require('gulp-util');
var clean = require('gulp-clean');
var jsdom = require('jsdom');
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
    
    // output filename
    '-o', 'out/index-<%= lang %>.html',
    
    // More options
    '-t', 'html5',                 // format used to write the output
    '--smart',                     // smart quotes and hyphens
    '--template', 'template.html', // HTML template to use
    '--css', 'css/main.min.css',   // CSS to link to from the output
    '--highlight-style', 'tango',  // highlighting syntax for code sections
];

const MODULE_REGEX = /^module(\d+).md$/;

/**
 * This function finds and returns all the input files in a given directory,
 * corresponding to the *.md files of a language edition. Only index.md and
 * module*.md files are returned, where * is any string with only digits. The
 * returned array contains the index.md in the first position (if one such file
 * exists) and the module*.md files sorted in numeric order after that.
 */
function getInputFiles(lang) {
    // Get all the files in the directory. Then assign to each a numeric value
    // for subsequent sorting purposes: `index.md` gets 0; `module*.md` gets the
    // numeric value of the `*`. Then, keep the files with a numeric value;
    // the rest are not valid for our purposes.
    var files = fs
        .readdirSync(lang)
        .reduce(function (current, item) {
            var value = false;
            
            if (item === 'index.md') {
                value = 0;
            }
            else {
                var match = MODULE_REGEX.exec(item);
                if (match !== null) {
                    value = parseInt(match[1])
                }
            }
            
            if (value !== false) {
                current.push([value, item]);
            }
            
            return current;
        }, []);
    
    // Sort the files using the numeric value
    files.sort(function(a, b) {
        return a[0] - b[0]
    });
    
    // Return only the file names, joined with the name of the directory
    return files.map(function(item) {
        return path.join(lang, item[1]);
    });
}

/**
 * This function returns a gulp pipeline that builds the index.html file from
 * the *.md files, specifically for a given language tag (en, pt, etc...),
 * thus building the main site of a given localization.
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
    
    return gulp.src(lang + '/*.md')
        .pipe(
            shell([ command.join(' ') ], {
                templateData: { lang }
            })
        )
        .on('end', function() {
            jsdom.env({
                file: 'out/index-' + lang + '.html',
                scripts: ['http://code.jquery.com/jquery.js'],
                done(err, window) {
                    var $ = window.$;
                    
                    // Replace all instances of '???' inside <code> elements with the
                    // HTML code:
                    // <span class="blank">?</span>
                    $('code').html(function () {
                        return $(this)
                            .html()
                            .replace(/\?\?\?/g, '<span class="blank">?</span>');
                    });

                    // 'print' is a builtin in python3 but a keyworkd in python2.
                    // Let's also make this change here
                    $('span.bu').each(function() {
                        if ($(this).text() == 'print') {
                            $(this).removeClass('bu');
                            $(this).addClass('kw');
                        }
                    });
                    
                    // Remove the extra jquery <script> element
                    $('script.jsdom').remove();
                    
                    // Write the resulting file back into its output filename
                    var newSource = $('html').html();
                    fs.writeFile(
                        'out/index-' + lang + '.html',
                        newSource,
                        function(err) {
                            if (err) throw err;
                        }
                    );
                }
            });
        });
}

gulp.task('build-en', function() {
    return buildIndex('en');
});

gulp.task('build-pt', function() {
    return buildIndex('pt');
});

gulp.task('sass', function() {
    var options = {
        outputStyle: 'compressed',
    };
    
    return gulp.src('styles/sass/*.scss')
        .pipe(sass(options).on('error', sass.logError))
        .pipe(gulp.dest('out/css'));
});

gulp.task('minify-css', function() {
    return gulp.src(['out/css/*.css', '!out/css/main.min.css'])
        .pipe(cleanCSS())
        .pipe(rename('main.min.css'))
        .pipe(gulp.dest('out/css'))
});

gulp.task('clean-css', function() {
    return gulp.src(['out/css/*.css', '!out/css/main.min.css'])
        .pipe(clean());
});

gulp.task('watch', function() {
    gulp.watch('styles/sass/*.scss', function() {
        gulpSequence('sass', 'minify-css', 'clean-css')();
    });
    gulp.watch('en/*.md', ['build-en']);
    gulp.watch('pt/*.md', ['build-pt']);
});
