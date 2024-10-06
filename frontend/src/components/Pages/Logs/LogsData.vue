<script setup lang="ts">
import type { ILogData } from '@/types/ILogs'

interface IProps {
  data: ILogData
}
defineProps<IProps>();
</script>

<template>
  <div class="logs-data">
    <p>Last updated: {{ data.lastUpdated }}</p>
    <div class="logs-data__wrapper">
      <template v-if="data.logs.length">
        <ul class="logs-data__list">
          <li v-for="(item, index) in data.logs" :key="`logData-${index}`" class="logs-data__item">
            {{ item }}
          </li>
        </ul>
      </template>
      <p v-else class="logs-data__empty">Log files is empty</p>
    </div>
  </div>
</template>

<style scoped lang="scss">
.logs-data {
  width: 100%;
  margin: 0 auto;
  display: grid;
  &__wrapper {
    border-radius: 10px;
    min-height: 400px;
    background: #e8e8e8;
    padding: 10px;
    overflow-x: hidden;
    overflow-y: auto;
    width: 100%;
  }
  &__list {
    display: grid;
    max-height: 600px;
    padding: 0;
    list-style: none;
  }
  &__item {
    word-break: break-all;
    margin: 4px;
    width: fit-content;
  }
  &__empty {
    text-align: center;
  }
}
</style>