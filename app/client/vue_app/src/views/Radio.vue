<template>
  <div class="radio-container">
    <h1>Radio</h1>
    <p>
        Choose station:
        <a href="" @click.prevent="playRadio">Play</a> |
        <a href="" @click.prevent="stopRadio">Stop</a>

        <form>
            <select name="stations">
              <option value="hr-info">hr Info</option>
              <option value="ndr-1-sh">NDR 1 SH</option>
              <option value="br-heimat">br Heimat</option>
              <option value="wfuv">WFUV</option>
            </select>
        </form>
        <p v-for="r in resources" :key="r.timestamp">
          Server Timestamp: {{r.timestamp | formatTimestamp }}<br/>
          Command: {{r.command}}<br/>
          Args: {{r.args}}
        </p>
    </p>
  </div>
</template>

<script>
import $backend from '../backend'

export default {
  name: 'about',
  data () {
    return {
      resources: [],
      error: ''
    }
  },
  methods: {
    playRadio () {
      $backend.playRadio()
        .then(responseData => {
          this.resources.push(responseData)
        }).catch(error => {
          this.error = error.message
        })
    },
    stopRadio () {
      $backend.stopRadio()
      .then(responseData => {
        this.resources.push(responseData)
      }).catch(error => {
        this.error = error.message
      })
    }
  }
}
</script>

<style lang="scss">

</style>
