---
pageClass: about-page
description: 'The biography and information about me.'
avatar: /profile.jpg
head: Aaron Lamoreaux
info: Computer Science and Math major at UT Austin
interests: 'Interests: Competitive Programming, Chinese, and Climbing'
socials:
- title: github
  link: https://github.com/lamoreauxaj
- title: linkedin
  link: https://www.linkedin.com/in/aaron-l-b8b3a6124/
- title: email
  link: 'mailto:lamoreauxaj[at]gmail.com'
footer: Made with ♥ by Aaron. Powered by VuePress
---

<AboutCard :frontmatter="$page.frontmatter" >

Software engineer in NYC

</AboutCard>

<style lang="stylus">

.theme-container.about-page .page
  background-color #e6ecf0
  min-height calc(100vh)
  
  .last-updated
    display none

</style>
