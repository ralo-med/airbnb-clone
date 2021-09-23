import gulp from "gulp";
import del from "del";
import gulpSass from "gulp-sass";
import nodeSass from "node-sass";
import minify from "gulp-csso";
import postCSS from "gulp-postcss";
import autoprefixer from "gulp-autoprefixer";
import tailwindcss from "tailwindcss";

const sass = gulpSass(nodeSass);

const routes = {
  css: {
    src: "assets/scss/styles.scss",
    dest: "static/css",
    watch: "assets/scss/*",
  },
};

const styles = () =>
  gulp
    .src(routes.css.src)
    .pipe(sass().on("error", sass.logError))
    .pipe(
      autoprefixer({
        flexbox: true,
        grid: "autoplace",
      })
    )
    .pipe(postCSS([tailwindcss]))
    .pipe(minify())
    .pipe(gulp.dest(routes.css.dest));

const watch = () => {
  gulp.watch(routes.css.watch, { usePolling: true }, styles);
};

const clean = () => del(["static/styles.css"]);

const assets = gulp.series([styles]);

const prepare = gulp.series([clean]);

const live = gulp.parallel([watch]);

export const build = gulp.series([prepare, assets]);
export const dev = gulp.series([build, live]);
