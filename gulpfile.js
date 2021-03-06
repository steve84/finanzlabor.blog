var gulp = require('gulp');
var uglify = require('gulp-uglify-es').default;
var minifycss = require('gulp-clean-css');
var htmlmin = require('gulp-htmlmin');
var imagemin = require('gulp-imagemin');
var replace = require('gulp-replace');
var pump = require('pump');
var Hexo = require('hexo');

function exec_hexo(fn, args, cb) {
  inhex.then(() => hexo.call(fn, args))
      .then(() => hexo.exit())
      .then(() => cb())
      .catch((err) => {
        console.log(err);
        hexo.exit(err);
        return cb(err);
      });
};

var hexo = new Hexo(process.cwd(), {});
inhex = hexo.init();

gulp.task('set_variables', (cb) => {
  pump([
    gulp.src(['themes/icarus/_config.yml']),
    replace('GULP_GITALK', '9992e6cc1af00d3d93f29c54bafba47ccc8df155'),
    replace('GULP_GA', 'UA-146513464-1'),
    gulp.dest('themes/icarus')
  ], cb);
});

gulp.task('reset_variables', (cb) => {
  pump([
    gulp.src(['themes/icarus/_config.yml']),
    replace('9992e6cc1af00d3d93f29c54bafba47ccc8df155', 'GULP_GITALK'),
    replace('UA-146513464-1', 'GULP_GA'),
    gulp.dest('themes/icarus')
  ], cb);
});

gulp.task('hexo-clean', (cb) => { exec_hexo('clean', {}, cb); })

gulp.task('hexo-generate', (cb) => { exec_hexo('generate', {watch : false}, cb); })

gulp.task('js-compress', (cb) => {
  pump([
    gulp.src('./public/**/*.js'),
    uglify(),
    gulp.dest('./public')
  ], cb);
});

gulp.task('minify-css', (cb) => {
  pump([
    gulp.src('./public/**/*.css'),
    minifycss({ compatibility: 'ie8' }),
    gulp.dest('./public')
  ], cb);
});

gulp.task('minify-html', (cb) => {
  pump([
    gulp.src('./public/**/*.html'),
    htmlmin({
      minifyJS : true,
      minifyCSS : true,
      minifyURLs : true,
      removeComments : true,
      removeRedundantAttributes : true,
      sortAttributes : true,
      sortClassName : true
    }),
    gulp.dest('./public')
  ], cb);
});

gulp.task('minify-img', (cb) => {
  pump([
    gulp.src('./public/images/**/*'),
    imagemin([
      imagemin.gifsicle({interlaced: true}),
      imagemin.jpegtran({progressive: true}),
      imagemin.optipng({optimizationLevel: 5}),
      imagemin.svgo({
        plugins: [
          {removeViewBox: true},
          {cleanupIDs: false}
        ]
      })
    ]),
    gulp.dest('./public/images')
  ], cb);
});

gulp.task('compress', gulp.series('js-compress', 'minify-css', 'minify-html', 'minify-img'));

gulp.task('generate', gulp.series('set_variables', 'hexo-clean', 'hexo-generate', 'reset_variables'));

gulp.task('default', gulp.series('generate', 'compress'));
