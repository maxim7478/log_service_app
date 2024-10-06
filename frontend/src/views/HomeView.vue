<script setup lang="ts">
import LogIcon from '@/components/icons/LogIcon.vue'
import UiButton from '@/components/Ui/UiButton.vue'
import { useRouter } from 'vue-router'

const router = useRouter();
const onToLogs = () => {
  router.push('logs')
}
</script>

<template>
  <div class="home-page">
    <div class="home-page__header">
      <log-icon height="50"/>
      <h1>Logs Note</h1>
    </div>
    <div class="home-page__content">
      <ui-button is-border is-round @click="onToLogs">Check Logs</ui-button>
    </div>
  </div>
</template>

<style scoped lang="scss">
.home-page {
  padding: 20px;
  text-align: center;
  &__header {
    color: #274D7E;
    fill: #274D7E;
    display: flex;
    align-items: center;
    margin-bottom: 20px;
  }
}
</style>
