<script setup lang="ts">
import { onBeforeUnmount, ref } from 'vue'
import { useDebounce } from '@/composables/useDebounce'
import logApi from '@/services/api'
import LogsData from '@/components/Pages/Logs/LogsData.vue'
import UiInputNumber from '@/components/Ui/UiInputNumber.vue'
import UiButton from '@/components/Ui/UiButton.vue'
import type { ILogData, ILogsBackend } from '@/types/ILogs'

const logData = ref<ILogData>({
  logs: [],
  lastUpdated: "Not updated"
})
const loading = ref(false)
const countRows = ref(5)
const isStart = ref(false)
let timer: number = 0;

const getLogs = async () => {
  if (isStart.value) {
    const data: ILogsBackend = await logApi.getLogData({ lines: countRows.value })
    logData.value.logs = [...data.logs]
    logData.value.lastUpdated = data.date_time
  }
}

const changeState = async () => {
  isStart.value = !isStart.value
  clearInterval(timer as number)
  if (isStart.value) {
    await getLogs()
    timer = setInterval(async () => {
      await getLogs()
    }, 5000)
  }
}

const search = useDebounce(getLogs, 500)

onBeforeUnmount(() => {
  clearInterval(timer as number)
})
</script>

<template>
  <div class="pooling-page">
    <div class="pooling-page__top">
      <ui-input-number
        v-model.number="countRows"
        placeholder="Count logs"
        @input="search"
      />
      <ui-button
        theme="primary"
        is-round
        is-border
        @click="changeState"
      >
        {{ isStart ? 'Stop' : 'Start' }}
      </ui-button>
    </div>
    <p v-if="loading">Загрузка...</p>
    <logs-data v-else :data="logData" />
  </div>
</template>

<style scoped lang="scss">
.pooling-page {
  width: 100%;
  &__top {
    display: flex;
    gap: 4px;
    flex-wrap: wrap;
  }
}
</style>