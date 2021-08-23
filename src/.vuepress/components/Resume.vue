<template>
  <div class="resume">
    <div class="left-column">
      <h1 class="name">
        {{ name }}
      </h1>
      <div class="socials">
        <div class="social" v-for="social in socials">
          <img :src="social.icon" alt="github"/>
          {{ social.content }}
        </div>
      </div>
      <ResumeSection class="section" :section="sections[section]" v-for="section in left"/>
    </div>
    <div class="right-column">
      <ResumeSection class="section" :section="sections[section]" v-for="section in right"/>
    </div>
  </div>
</template>

<script>
import resume from '../../resume.yaml';

export default {
  data() {
    return resume;
  }
};
</script>

<style scoped lang="scss">
.resume {
  font-size: 14px;
  font-family: "lucida grande", "lucida sans unicode", lucida, "Helvetica Neue", Helvetica, Arial, sans-serif;
  background-color: white;
  position: absolute;
  left: 0;
  top: 0;
  width: 815px;
  height: 1055px;
  display: flex;
  flex-direction: row;
  margin: 0 !important;
  .section {
    margin-bottom: -3px;
  }
  .left-column {
    background-color: #f8f8f8;
    width: 37%;
    padding: 0;
    display: flex;
    flex-direction: column;
    .name {
      color: white;
      background-color: #413950;
      height: 100px;
      margin: 0;
      padding: 5px 20px 0px 20px;
      margin-bottom: -5px;
      line-height: normal;
    }
    .socials {
      display: flex;
      flex-direction: column;
      align-items: left;
      padding: 5px 20px;
      margin-bottom: 5px;
      background-color: #60596c;
      color: white;
      .social {
        display: flex;
        flex-direction: row;
        align-items: center;
        font-family: Courier New, Courier, monospace;
        font-weight: 550;
        margin: 3px 0;
        img {
          filter: invert(100%);
          width: 1.0rem;
          margin: 0 0.3rem 0 0;
          cursor: pointer;
        }
      }
    }
  }
  .right-column {
    width: 63%;
    padding-top: 5px;
  }
}
</style>
