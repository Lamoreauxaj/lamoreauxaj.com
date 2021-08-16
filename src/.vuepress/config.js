module.exports = {
  title: "Aaron Lamoreaux",
  description: "Aaron Lamoreaux's Personal Webpage",
  head: [
    ["link", { rel: "icon", href: `/logo.png` }],
    ["link", { rel: "stylesheet", href: "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.5.1/katex.min.css" }]
  ],
  base: "/",
  dest: "./dist",

  themeConfig: {
    search: false,
    nav: [],
    sidebar: {}
  },

  markdown: {
    anchor: { permalink: false },
    extendMarkdown: md => {
      md.use(require('markdown-it-katex'))
      md.use(require('markdown-it-figure'))
      md.use(require('markdown-it-html5-embed'), { html5embed: { useImageSyntax: true, useLinkSyntax: true } })
    }
  }
}
