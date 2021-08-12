<template>
  <div class="profile">
    <div v-if="data.profile" class="image">
      <img :src="$withBase(data.profile)" alt="">
    </div>
    <div class="info">
      <div class="name">
        {{ data.name }}
      </div>
      <div class="socials">
        <img src="/icons/github.svg" alt="github">
        lamoreauxaj
      </div>
      <div class="contact">
        <div class="email" title="Contact me">{{ data.email }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ['image', 'cv', 'frontmatter'],

  computed: {
    data() {
      return this.frontmatter;
    }
  }
};
</script>

<style lang="stylus">
@import './styles/config.styl'

.download
  cursor: pointer

.profile
  display flex
  flex-direction row
  align-items stretch
  .image
    max-width 120px
    img
      border-radius 50%
      padding 2px
      border 1px solid #f2f3f3
  .info
    display flex
    flex 1 1
    flex-direction column
    .name
      font-size 1.85rem
      font-weight 600
    .socials
      display flex
      flex-direction row
      align-items: center
      img
        width 1.0rem
        margin 0 0.3rem 0 0
        cursor pointer
    .contact
      .title
        font-size 1.2rem
        font-weight 400
      .email
        font-family Courier New, Courier, monospace

@media (max-width: $MQMobileNarrow)
  .profile
    .image
      max-width 100px
</style>
