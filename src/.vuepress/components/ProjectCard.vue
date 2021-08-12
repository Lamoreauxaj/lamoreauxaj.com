<template>
  <div class="project-card">
    <div class="header">
      <div class="left-header">
        <b class="title">{{ title }}</b>
      </div>
      <div class="right-header">
        <i class="location">{{ location }}</i>
        |
        <span class="date">{{ date }}</span>
      </div>
    </div>
    <slot/>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      required: true
    },
    location: {
      type: String,
      required: false
    },
    date: {
      type: String,
      required: false
    }
  }
};
</script>

<style lang="stylus">
.header
  display: flex
  flex-direction: row
  justify-content: space-between
  .left-header
    max-width: 60%
  .right-header
    display: flex
    flex-direction: row
    flex-wrap: wrap
    justify-content: flex-end
    text-align: right
    .location
      display: inline-block
      margin-right: 3px
    .date
      margin-left: 3px
      max-width: 70%
      display: inline-block

.project-card
  ul
    margin-top: 2px
</style>
