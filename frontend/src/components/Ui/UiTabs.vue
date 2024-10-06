<script setup lang="ts">
import { ref } from 'vue'

interface ITabs {
  id: string | number;
  title: string;
  key: string;
}

interface IEmit {
  (event: "click-tab", value: string): void;
  (event: "select"): void;
}

interface IProps {
  list: ITabs[];
  activeDefault?: string;
}
const emit = defineEmits<IEmit>();
const props = withDefaults(defineProps<IProps>(), {
  activeDefault: "",
});

const activeTab = ref(
  props.activeDefault ? props.activeDefault : props.list[0].key
);
const onClickTab = (value: string) => {
  if (activeTab.value === value) return;
  activeTab.value = value;
  emit("click-tab", value);
};
</script>

<template>
  <div class="ui-tabs">
    <ul class="ui-tabs__list">
      <li
        v-for="(tab, index) in list"
        :key="`ui-tab-${index}`"
        :class="[
					'ui-tabs__item',
					activeTab === tab.key ? `ui-tabs__item--active` : '',
				]"
        @click="onClickTab(tab.key)"
      >
        {{ tab.title }}
      </li>
    </ul>
  </div>
</template>

<style scoped lang="scss">
.ui-tabs {
  border-radius: 4px;
  overflow: hidden;
  width: max-content;
  min-height: fit-content;
  &__list {
    display: flex;
    align-items: center;
    flex-flow: row wrap;
    padding: 0;
    list-style-type: none;
  }
  &__item {
    font-size: 14px;
    line-height: 18px;
    cursor: pointer;
    border-top: 2px solid transparent;
    background: white;
    padding: 12px 16px;
    border-bottom: 2px solid #dcdcdc;
    color: black;
    &--active {
      color: #274D7E;
      border-bottom: 2px solid #274D7E;
      font-weight: bold;
    }
  }
}
</style>