// Build: npx tailwindcss@3 -i tailwind.input.css -o styles.css --minify
module.exports = {
  "darkMode": "class",
  "theme": {
    "extend": {
      "colors": {
        "surface": "rgb(var(--color-surface) / <alpha-value>)",
        "background": "rgb(var(--color-background) / <alpha-value>)",
        "surface-dim": "rgb(var(--color-surface-dim) / <alpha-value>)",
        "surface-bright": "rgb(var(--color-surface-bright) / <alpha-value>)",
        "surface-container-lowest": "rgb(var(--color-surface-container-lowest) / <alpha-value>)",
        "surface-container-low": "rgb(var(--color-surface-container-low) / <alpha-value>)",
        "surface-container": "rgb(var(--color-surface-container) / <alpha-value>)",
        "surface-container-high": "rgb(var(--color-surface-container-high) / <alpha-value>)",
        "surface-container-highest": "rgb(var(--color-surface-container-highest) / <alpha-value>)",
        "surface-variant": "rgb(var(--color-surface-variant) / <alpha-value>)",
        "on-surface": "rgb(var(--color-on-surface) / <alpha-value>)",
        "on-background": "rgb(var(--color-on-background) / <alpha-value>)",
        "on-surface-variant": "rgb(var(--color-on-surface-variant) / <alpha-value>)",
        "outline": "rgb(var(--color-outline) / <alpha-value>)",
        "outline-variant": "rgb(var(--color-outline-variant) / <alpha-value>)",
        "inverse-surface": "rgb(var(--color-inverse-surface) / <alpha-value>)",
        "inverse-on-surface": "rgb(var(--color-inverse-on-surface) / <alpha-value>)",
        "primary": "rgb(var(--color-primary) / <alpha-value>)",
        "primary-container": "rgb(var(--color-primary-container) / <alpha-value>)",
        "on-primary": "rgb(var(--color-on-primary) / <alpha-value>)",
        "on-primary-container": "rgb(var(--color-on-primary-container) / <alpha-value>)",
        "primary-fixed": "rgb(var(--color-primary-fixed, var(--color-primary)) / <alpha-value>)",
        "primary-fixed-dim": "rgb(var(--color-primary-fixed-dim, var(--color-primary)) / <alpha-value>)",
        "on-primary-fixed": "rgb(var(--color-on-primary-fixed, var(--color-on-primary)) / <alpha-value>)",
        "on-primary-fixed-variant": "rgb(var(--color-on-primary-fixed-variant, var(--color-on-primary)) / <alpha-value>)",
        "secondary": "rgb(var(--color-secondary) / <alpha-value>)",
        "secondary-container": "rgb(var(--color-secondary-container) / <alpha-value>)",
        "on-secondary": "rgb(var(--color-on-secondary) / <alpha-value>)",
        "on-secondary-container": "rgb(var(--color-on-secondary-container) / <alpha-value>)",
        "secondary-fixed": "rgb(var(--color-secondary-fixed, var(--color-secondary)) / <alpha-value>)",
        "secondary-fixed-dim": "rgb(var(--color-secondary-fixed-dim, var(--color-secondary)) / <alpha-value>)",
        "on-secondary-fixed": "rgb(var(--color-on-secondary-fixed, var(--color-on-secondary)) / <alpha-value>)",
        "on-secondary-fixed-variant": "rgb(var(--color-on-secondary-fixed-variant, var(--color-on-secondary)) / <alpha-value>)",
        "tertiary": "rgb(var(--color-tertiary) / <alpha-value>)",
        "tertiary-container": "rgb(var(--color-tertiary-container) / <alpha-value>)",
        "on-tertiary": "rgb(var(--color-on-tertiary) / <alpha-value>)",
        "on-tertiary-container": "rgb(var(--color-on-tertiary-container) / <alpha-value>)",
        "tertiary-fixed": "rgb(var(--color-tertiary-fixed, var(--color-tertiary)) / <alpha-value>)",
        "tertiary-fixed-dim": "rgb(var(--color-tertiary-fixed-dim, var(--color-tertiary)) / <alpha-value>)",
        "on-tertiary-fixed": "rgb(var(--color-on-tertiary-fixed, var(--color-on-tertiary)) / <alpha-value>)",
        "on-tertiary-fixed-variant": "rgb(var(--color-on-tertiary-fixed-variant, var(--color-on-tertiary)) / <alpha-value>)",
        "error": "rgb(var(--color-error) / <alpha-value>)",
        "error-container": "rgb(var(--color-error-container) / <alpha-value>)",
        "on-error": "rgb(var(--color-on-error) / <alpha-value>)",
        "on-error-container": "rgb(var(--color-on-error-container) / <alpha-value>)",
        "surface-tint": "rgb(var(--color-primary) / <alpha-value>)",
        "inverse-primary": "rgb(var(--color-inverse-primary, var(--color-primary-container)) / <alpha-value>)"
      },
      "borderRadius": {
        "DEFAULT": "var(--r-md, 1rem)",
        "lg": "var(--r-lg, 2rem)",
        "xl": "var(--r-xl, 3rem)",
        "full": "9999px"
      },
      "spacing": {
        "margin-sm": "1rem",
        "margin-lg": "4rem",
        "margin": "1.5rem",
        "space-md": "1rem",
        "gutter": "1.5rem",
        "gutter-lg": "2rem",
        "gutter-sm": "1rem",
        "space-lg": "1.5rem",
        "space-sm": "0.5rem",
        "space-xs": "0.25rem",
        "space-xl": "2rem"
      },
      "fontFamily": {
        "label-md": [
          "var(--md-sys-code-font-family)"
        ],
        "body-sm": [
          "var(--md-sys-body-font-family)"
        ],
        "label-sm": [
          "var(--md-sys-code-font-family)"
        ],
        "headline-md": [
          "var(--md-sys-typescale-font-family)"
        ],
        "display-md": [
          "var(--md-sys-typescale-font-family)"
        ],
        "headline-lg": [
          "var(--md-sys-typescale-font-family)"
        ],
        "display-lg": [
          "var(--md-sys-typescale-font-family)"
        ],
        "title-md": [
          "var(--md-sys-body-font-family)"
        ],
        "title-sm": [
          "var(--md-sys-body-font-family)"
        ],
        "body-md": [
          "var(--md-sys-body-font-family)"
        ],
        "headline-sm": [
          "var(--md-sys-typescale-font-family)"
        ],
        "title-lg": [
          "var(--md-sys-typescale-font-family)"
        ],
        "display-sm": [
          "var(--md-sys-typescale-font-family)"
        ],
        "headline-lg-mobile": [
          "var(--md-sys-typescale-font-family)"
        ],
        "body-lg": [
          "var(--md-sys-body-font-family)"
        ],
        "label-lg": [
          "var(--md-sys-code-font-family)"
        ]
      },
      "fontSize": {
        "label-md": [
          "12px",
          {
            "lineHeight": "16px",
            "letterSpacing": "0.03em",
            "fontWeight": "500"
          }
        ],
        "body-sm": [
          "12px",
          {
            "lineHeight": "16px",
            "letterSpacing": "0.02em",
            "fontWeight": "400"
          }
        ],
        "label-sm": [
          "10px",
          {
            "lineHeight": "14px",
            "letterSpacing": "0.04em",
            "fontWeight": "500"
          }
        ],
        "headline-md": [
          "28px",
          {
            "lineHeight": "36px",
            "fontWeight": "600"
          }
        ],
        "display-md": [
          "45px",
          {
            "lineHeight": "52px",
            "letterSpacing": "-0.02em",
            "fontWeight": "700"
          }
        ],
        "headline-lg": [
          "32px",
          {
            "lineHeight": "40px",
            "letterSpacing": "-0.01em",
            "fontWeight": "600"
          }
        ],
        "display-lg": [
          "57px",
          {
            "lineHeight": "64px",
            "letterSpacing": "-0.025em",
            "fontWeight": "700"
          }
        ],
        "title-md": [
          "16px",
          {
            "lineHeight": "24px",
            "letterSpacing": "0.01em",
            "fontWeight": "600"
          }
        ],
        "title-sm": [
          "14px",
          {
            "lineHeight": "20px",
            "letterSpacing": "0.01em",
            "fontWeight": "600"
          }
        ],
        "body-md": [
          "14px",
          {
            "lineHeight": "20px",
            "letterSpacing": "0.015em",
            "fontWeight": "400"
          }
        ],
        "headline-sm": [
          "24px",
          {
            "lineHeight": "32px",
            "fontWeight": "500"
          }
        ],
        "title-lg": [
          "22px",
          {
            "lineHeight": "28px",
            "fontWeight": "500"
          }
        ],
        "display-sm": [
          "36px",
          {
            "lineHeight": "44px",
            "letterSpacing": "-0.015em",
            "fontWeight": "600"
          }
        ],
        "headline-lg-mobile": [
          "28px",
          {
            "lineHeight": "36px",
            "letterSpacing": "-0.01em",
            "fontWeight": "600"
          }
        ],
        "body-lg": [
          "16px",
          {
            "lineHeight": "24px",
            "letterSpacing": "0.01em",
            "fontWeight": "400"
          }
        ],
        "label-lg": [
          "14px",
          {
            "lineHeight": "20px",
            "letterSpacing": "0.02em",
            "fontWeight": "500"
          }
        ]
      }
    }
  },
  "content": [
    "./index.html"
  ]
};
