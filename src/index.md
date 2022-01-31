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
actions:
- text: CV
  link: /cv.pdf
footer: Made with ♥ by Aaron. Powered by VuePress
---

<AboutCard :frontmatter="$page.frontmatter" >

Future software engineer intern in Hong Kong, graduating in Dec 2022. Current classes
at UT Austin include Natural Language Processing, Computer Graphics, and Chinese.

</AboutCard>

<style lang="stylus">

.theme-container.about-page .page
  background-color #e6ecf0
  min-height calc(100vh)
  
  .last-updated
    display none

</style>
