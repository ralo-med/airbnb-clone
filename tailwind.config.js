const colors = require("tailwindcss/colors");

module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    colors: {
      black: colors.black,
      red: colors.red,
      gray: colors.gray,
      white: colors.white,
      teal: colors.teal,
      yellow: colors.yellow,
    },
    extend: {
      spacing: {
        "40vh": "40vh",
        "50vh": "50vh",
        "75vh": "75vh",
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
