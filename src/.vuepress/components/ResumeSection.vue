<template>
  <div class="section">
    <div class="title-container">
      <h3 class="title">{{ section.title }}</h3>
      <hr/>
    </div>
    <div class="items" v-if="section.type === 'single'" v-html="md.render(section.content)">
    </div>
    <div class="projects" v-if="section.type === 'project'">
      <div class="project" v-for="item in section.content">
        <div class="header">
          <b class="project-title">{{ item.title }}</b>
          <span class="project-info" v-if="item.location">
            <i class="location">{{ item.location }}</i>
            |
            <span class="date">{{ item.date }}</span>
          </span>
          <span class="project-info" v-else>
            <span class="date">{{ item.date }}</span>
          </span>
        </div>
        <div v-html="md.render(item.description)" v-if="item.description"/>
      </div>
    </div>
  </div>
</template>

<script>
import MarkdownIt from 'markdown-it';
const md = new MarkdownIt();

export default {
  props: {
    section: {
      required: true,
      type: Object
    }
  },
  data() {
    return { md };
  }
};
</script>

<style scoped lang="scss">
::v-deep ul {
  list-style: none;
  margin: 0 0 0 5px;
  padding-left: 1em;
}
::v-deep li {
  margin: 4px 0;
  padding: 0;
  line-height: normal;
}
::v-deep li:before {
  content: "-";
  color: #2c3e50;
  width: 1em;
  margin-left: -1em !important;
  margin-right: 3px;
}
::v-deep .items p {
  margin: 5px;
  line-height: normal;
}
::v-deep .projects p {
  margin: 5px;
  line-height: normal;
}
.section {
  margin: 15px 20px 0px 20px;
  .title-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    .title {
      margin: 0;
      white-space: nowrap;
    }
    hr {
      flex-shrink: 100%;
      margin-left: 15px;
      width: 100%;
    }
  }
  .items {
    margin: 0 0px;
    padding-left: -1em;
  }
  .projects {
    margin-left: 5px;
    .project {
      margin-top: 7px;
      .header {
        display: flex;
        flex-direction: row;
        width: 100%;
        justify-content: space-between;
        align-items: center;
        b {
          max-width: 65%;
          display: inline-block;
          flex-shrink: 1;
        }
        .project-info {
          flex-shrink: 100;
          max-width: 70%;
          text-align: right;
          display: flex;
          flex-direction: row;
          flex-wrap: wrap;
          justify-content: flex-end;
          .location {
            margin-right: 3px;
            display: inline-block;
            white-space: nowrap;
          }
          .date {
            margin-left: 3px;
            display: inline-block;
            white-space: nowrap;
          }
        }
      }
    }
  }
}
</style>
