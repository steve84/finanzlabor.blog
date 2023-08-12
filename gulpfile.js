const gulp = require('gulp');
const uglify = require('gulp-uglify');
const minifycss = require('gulp-clean-css');
const htmlmin = require('gulp-htmlmin');
const replace = require('gulp-replace');
const imagemin = require('gulp-imagemin');
const pump = require('pump');
const Hexo = require('hexo');

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
    gulp.src(['_config.icarus.yml']),
    replace('GULP_GA', 'UA-146513464-1'),
    gulp.dest('./')
  ], cb);
});

gulp.task('reset_variables', (cb) => {
  pump([
    gulp.src(['_config.icarus.yml']),
    replace('UA-146513464-1', 'GULP_GA'),
    gulp.dest('./')
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
    gulp.src('./public/img/**/*'),
    imagemin([
      imagemin.gifsicle({interlaced: true}),
      imagemin.mozjpeg({quality: 75, progressive: true}),
      imagemin.optipng({optimizationLevel: 5}),
      imagemin.svgo({
        plugins: [
          {removeViewBox: true},
          {cleanupIDs: false}
        ]
      })
    ]),
    gulp.dest('./public/img/')
  ], cb);
});

gulp.task('minify-gallery', (cb) => {
  pump([
    gulp.src('./public/gallery/**/*'),
    imagemin([
      imagemin.gifsicle({interlaced: true}),
      imagemin.mozjpeg({quality: 75, progressive: true}),
      imagemin.optipng({optimizationLevel: 5}),
      imagemin.svgo({
        plugins: [
          {removeViewBox: true},
          {cleanupIDs: false}
        ]
      })
    ]),
    gulp.dest('./public/gallery/')
  ], cb);
});


gulp.task('compress', gulp.series('js-compress', 'minify-css', 'minify-html', 'minify-img', 'minify-gallery'));

gulp.task('generate', gulp.series('set_variables', 'hexo-clean', 'hexo-generate', 'reset_variables'));

gulp.task('default', gulp.series('generate', 'compress'));
