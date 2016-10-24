var fs = require('file-system');
var gulp = require('gulp');
var sass = require('gulp-sass');
var shell = require('gulp-shell');
var gutil = require('gulp-util');
var clean = require('gulp-clean');
var jsdom = require("jsdom");
var rename = require('gulp-rename');
var cleanCSS = require('gulp-clean-css');
var gulpSequence = require('gulp-sequence')

/**
 * The shell command that builds a set of *.md files into an *.html file.
 */
const PANDOC_COMMAND = [
    // executable
    'pandoc',
    
    // input filenames
    '<%= lang %>/index.md',
    '<%= lang %>/module1.md',
    '<%= lang %>/module2.md',
    '<%= lang %>/module3.md',
    '<%= lang %>/module4.md',
    '<%= lang %>/module5.md',
    '<%= lang %>/module6.md',
    '<%= lang %>/module7.md',
    
    // output filename
    '-o', 'out/index-<%= lang %>.html',
    
    // More options
    '-t', 'html5',                 // format used to write the output
    '--smart',                     // smart quotes and hyphens
    '--template', 'template.html', // HTML template to use
    '--css', 'css/main.min.css',   // CSS to link to from the output
    '--highlight-style', 'tango',  // highlighting syntax for code sections
].join(' ');

/**
 * This function returns a gulp pipeline that builds the index.html file from
 * the *.md files, specifically for a given language tag (en, pt, etc...),
 * thus building the main site of a given localization.
 */
function buildIndex(lang) {
    gulp.src(lang + '/*.md')
        .pipe(
            shell([ PANDOC_COMMAND ], {
                templateData: { lang }
            })
        );
    
    jsdom.env({
        file: 'out/index-' + lang + '.html',
        scripts: ['http://code.jquery.com/jquery.js'],
        done(err, window) {
            var $ = window.$;
            
            // Replace all instances of "???" inside <code> elements with the HTML code:
            // <span class="blank">?</span>
            $('code').html(function () {
                return $(this).html().replace(/\?\?\?/g, '<span class="blank">?</span>');
            });

            // 'print' is a builtin in python3 but a keyworkd in python2.
            // Let's make sure this change happens
            $('span.bu').each(function() {
                if ($(this).text() == 'print') {
                    $(this).removeClass('bu');
                    $(this).addClass('kw');
                }
            });
            
            $('script.jsdom').remove();
            
            var newSource = $('html').html();
            
            process.nextTick(function() {
                fs.writeFile(
                    'out/index-' + lang + '.html',
                    newSource,
                    function(err) {
                        if (err) throw err;
                    }
                );
            });
        }
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
