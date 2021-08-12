---
pageClass: home-page

name: Aaron Lamoreaux

socials:
  - title: github
    icon: "/icons/github.svg"
    link: https://github.com/lamoreauxaj
  - title: linkedin
    icon: "/icons/linkedin-mono.svg"
    link: https://www.linkedin.com/in/aaron-l-b8b3a6124

bio: Computer Science and Mathematics major at UT Austin
email: lamoreauxaj@gmail.com
---

<ClientOnly>
<Resume :frontmatter="$page.frontmatter">
<template v-slot:left>

### Education

<ProjectCard title="Computer Science B.S, Math B.S" location="UT Austin" date="Aug 2019-Dec 2022">

Member of UTPC, ISSS, and ACM. GPA: 4.0. </br>
Working on independent research project with Dr. Scott Aaronson.

#### Coursework:

- Operating Systems (Honors)
- Algorithms (Honors)
- Quantum Complexity Theory (Graduate)
- Quantum Information Science (Honors)
- Sublinear Algorithms (Graduate)
- System Architecture (Honors)
- Automated Logical Reasoning (Graduate)
- Real Analysis II
- Topology I
- Abstract Algebra (upcoming)
- Theory of Computation (upcoming)

</ProjectCard>


### Teaching Experience

- USACO Silver Instructor at Alphastar (Dec 2019, 2020)
- Algorithms TA (Spring 2021)
- Private USACO Tutoring (Feb 2020-Nov 2020)

### Awards

- USAJMO Qualifier 2017
- AIME Qualifier 3x
- USACO Finalist 2019
- UIL CS State Champions 2019
- ICPC World Finalist 2020
- Top 500 Putnam
- Codeforces Division 1 (2271)
- Mathworks Math Modeling Scholarship
- UT Distinguished College Scholar
- Second Year Excellence Award UT
- HackDFW Finalist 2019
- HackTX Finalist 2019

### Skills

Proficient: Java, C, C++, Python, JavaScript, OCaml, LaTeX

Familiar: Haskell, Kotlin, Perl, Assembly, Bash, Pig

### Languages

- English (fluent)
- Chinese (intermediate)

</template>

### Work Experience

<ProjectCard title="Software Engineering Intern" location="Jane Street" date="Jun 2021-Aug 2021">

  - Added new indexers for webpages and Google Drive to internal search engine which is used by nearly the entire firm.
  - Implemented Pagerank in order to improve the search results.
  - Implemented an authenticated API proxy in order to communicate with 5 different exchanges. Managed rate limiting and authentication for requests. Deployed and used to write publishers for requested data.
  - Created library to interact with 6 SQL tables related to the cryptocurrency desk.
  
</ProjectCard>


<ProjectCard title="Undergraduate Research Assistant" location="UT Austin" date="Feb 2020-Nov 2020">

- Worked on project with Dr. Isil Dilllig to extract information from semi-structured documents (mostly focused on extracting information from webpages) based on user benchmarks by applying program synthesis techniques with neural components.

</ProjectCard>

<ProjectCard title="Data Science Intern" location="Department of Defense" date="Jun 2019-Aug 2019">

- Held Top Secret/SI/TK security clearance.
- Used Pig and Python to write analytics on large data sets.
- Created Jupyter notebooks used by other teams for discovery with cyber-security data sources.

</ProjectCard>

<ProjectCard title="Enterprise Technology Intern" location="State Farm" date="Jun 2018-Jul 2018">

- Worked on automatic testing tools for insurance policy software using Node.js mock data generation frameworks.
- Worked on React.js web app used to visualize and log tests for internal projects.

</ProjectCard>

<ProjectCard title="IT Systems Intern" location="State Farm" date="Jun 2017-Jul 2017">

- Automated system for pushing updates to internal Apple products.
- Automated system for data transfers in migration effort.
- Created pages to manipulate databases for integration testing workflows using Ember.js.

</ProjectCard>

### Research

<ProjectCard title="Quantum Streaming Algorithms" location="CS395T" date="Jan 2021-May 2021">

- Wrote a survey paper for Quantum Complexity Theory course.
- Covers literature on quantum streaming algorithms.
- Focused on frequency moments and proved a better lower bound and gave a quantum algorithm which exceeds classical for 3rd moments.

</ProjectCard>

<ProjectCard title="Web Question Answering with Neurosymbolic Program Synthesis" location="PLDI 2021" date="Feb 2020-Nov 2020">

- Implemented program synthesis tool, WebQA, for extracting information from heterogenous webpages. Created DSL which includes both neural and programmatic constructs in order to handle diverse schemas. Benchmarked against 25 different tasks across various domains.

</ProjectCard>

<ProjectCard title="Applying Peelable Hypergraph Constructions to Sparse Recovery" location="CS395T" date="Aug 2020-Dec 2020">

- Worked on a research project for Sublinear Algorithms.
- Focused on recent paper by Walzer, investigating whether we can use results related to peelability to get improve constants for sparse recovery algorithms.

</ProjectCard>

### Projects

<ProjectCard title="Experimental Geometer" location="HackTX 2019" date="Feb 2019-Present">

- Built a VR application in Unity which would render dynamic geometric diagrams that could be manipulated dynmically.
- The diagrams were created with a geometric scripting language that was Turing Complete and could construct any Euclidean construction, yet did not have real numbers.
- Continuing to develop the scripting language with compiler written in C++.

</ProjectCard>

</Resume>
</ClientOnly>

<style lang="stylus">

.theme-container.home-page .page
  font-size 12px
  font-family "lucida grande", "lucida sans unicode", lucida, "Helvetica Neue", Helvetica, Arial, sans-serif;
  p
    margin 0 0 0.5rem
  p, ul, ol
    line-height normal
  ul
    margin-top: 2px
  a
    font-weight normal
  .theme-default-content:not(.custom) > h2
    margin-bottom 0.5rem
  .theme-default-content:not(.custom) > h2:first-child + p
    margin-top 0.5rem
  .theme-default-content:not(.custom) > h3
    padding-top 4rem
  .theme-default-content
    max-width: 800px
    
  h1, h2, h3, h4, h5, h6
    margin-bottom: 0
    margin-top: 5px
    
  h3
    font-size: 18px

  /* Override */
  .md-card
    margin-top 0.5em
    .card-image
      padding 0.2rem
      img
        max-width 120px
        max-height 120px
    .card-content p
      -webkit-margin-after 0.2em

@media (max-width: 419px)
  .theme-container.home-page .page
    p, ul, ol
      line-height 1.5

    .md-card
      .card-image
        img 
          width 100%
          max-width 400px
</style>
