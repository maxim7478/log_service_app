<script setup lang="ts">
import { type Component, ref } from 'vue'
import { useRouter } from 'vue-router'
import UiTabs from '@/components/Ui/UiTabs.vue'
import PoolingPage from '@/components/Pages/Logs/PoolingPage.vue'
import WebSocketPage from '@/components/Pages/Logs/WebSocketPage.vue'
import UiButton from '@/components/Ui/UiButton.vue'

const tabs = [
  {
    id: 1,
    title: 'Pooling',
    key: 'pooling'
  },
  {
    id: 2,
    title: 'WebSocket',
    key: 'socket'
  }
]

const activeTab = ref('pooling')

const currentComponent: Record<string, Component> = {
  pooling: PoolingPage,
  socket: WebSocketPage,
}

const changeTab = (tab: string) => {
  activeTab.value = tab
}

const router = useRouter();
const onToHome = () => {
  router.push('/')
}
</script>

<template>
  <div class="logs-view">
    <div class="logs-view__header">
      <h1>Logs</h1>
    </div>
    <ui-button theme="second" is-round is-border @click="onToHome">Home</ui-button>
    <ui-tabs :list="tabs" :active-default="activeTab" @click-tab="changeTab"/>
    <component :is="currentComponent[activeTab]" />
  </div>
</template>

<style scoped lang="scss">
.logs-view {
  margin: 0 auto;
  display: flex;
  flex-flow: column;
  gap: 20px;
  padding: 20px;
  align-items: center;
  max-width: 100%;
  height: 100%;
  &__header {
    display: flex;
    align-items: center;
    color: #274D7E;
  }
  &__wrapper {
    border-radius: 10px;
    min-height: 400px;
    background: #d0d0d0;
    padding: 10px;
  }
}
</style>