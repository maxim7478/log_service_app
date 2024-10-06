<script setup lang="ts">
import { onBeforeUnmount, ref } from 'vue'
import { useDebounce } from '@/composables/useDebounce'
import LogsData from '@/components/Pages/Logs/LogsData.vue'
import UiInputNumber from '@/components/Ui/UiInputNumber.vue'
import type { ILogData, ILogsWsBackend } from '@/types/ILogs'

const link = import.meta.env.VITE_WS_URL + '/ws-logs/'
const socket = new WebSocket(link);

const logData = ref<ILogData>({
  logs: [],
  lastUpdated: "Not updated"
})
const loading = ref(false)
const countRows = ref(5)
const clientId = ref()


const sendData = () => {
  socket.send(JSON.stringify(
    {
      id: clientId.value || null,
      lines: countRows.value,
    }
  ));
}

socket.onopen = function() {
  sendData();
}

socket.onmessage = function(event) {
  const data: ILogsWsBackend = JSON.parse(event.data)
  logData.value.logs = data.logs;
  logData.value.lastUpdated = data.date_time;
  clientId.value = data.id;
};

socket.onerror = function(error) {
  console.log(`${error}`);
};

const onSendNewState = () => {
  if (countRows.value) {
    sendData();
  }
}

const search = useDebounce(onSendNewState, 500)

onBeforeUnmount(() => {
  socket.close()
})
</script>

<template>
  <div class="web-socket-page">
    <div class="web-socket-page__top">
      <ui-input-number
        v-model.number="countRows"
        placeholder="Count logs"
        @input="search"
      />
    </div>
    <p v-if="loading">Загрузка...</p>
    <logs-data v-else :data="logData" />
  </div>
</template>

<style scoped lang="scss">
.web-socket-page {
  width: 100%;
  &__top {
    display: flex;
    gap: 4px;
    flex-wrap: wrap;
  }
}
</style>