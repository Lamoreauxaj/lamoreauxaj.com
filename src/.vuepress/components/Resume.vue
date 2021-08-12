<template>
  <div class="resume-container">
    <div class="header">
      <h1>CV</h1>
      <a class="download" @click="onDownload">Download PDF</a>
    </div>
    <!-- <div class="warning-container" v-if="windowWidth < 864">
         <span class="warning">Please view with larger window width or download PDF.</span>
         </div> -->
    <div class="resume" ref="resume">
      <div class="column-container">
        <div class="left-column">
          <ProfileSection :frontmatter="frontmatter"/>
          <slot name="left"/>
        </div>
        <div class="right-column">
          <slot/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProfileSection from './ProfileSection.vue'
import { jsPDF } from 'jspdf'
import html2canvas from 'html2canvas'

export default {
  props: {
    frontmatter: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      windowWidth: window.innerWidth,
    }
  },
  mounted() {
    this.$nextTick(() => {
      window.addEventListener('resize', this.onResize)
    })
    // if (this.windowWidth < 864) this.$refs.resume.style.display = 'none'
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  },
  methods: {
    onResize() {
      this.windowWidth = window.innerWidth
      // if (this.windowWidth < 864) this.$refs.resume.style.display = 'none'
      // else this.$refs.resume.style.display = 'block'
    },
    onDownload() {
      const resume = this.$refs.resume
      html2canvas(resume, { scale: 4 }).then((canvas) => {
        const doc = new jsPDF({
          unit: "in",
          format: [8.5, 11]
        })
        const height = canvas.height / canvas.width * 8.5
        const img = canvas.toDataURL('image/png')
        doc.addImage(img, 'PNG', 0, 0, 8.5, height)
        doc.save('resume.pdf')
      })
    }
  }
}
</script>

<style scoped lang="stylus">
.resume-container
  margin-top: 20px !important
  width: 800px
  .warning-container
    text-align: center
    .warning
      color: red
  .header
    display: flex
    flex-direction: column
    align-items: center
    border-bottom: 1px #eaecef solid
    margin-bottom: 10px
    h1
      border: none
    .download
      cursor: pointer
      font-size: 14px
  .resume
    padding: 20px
    width: 760px
    .column-container
      display: flex
      flex-direction: row
      justify-content: center
      .left-column
        width: 35%
        padding-right: 10px
      .right-column
        width: 65%
        margin-left: 10px
</style>
