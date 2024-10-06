<script setup lang="ts">
defineProps<{
  modelValue: number;
  placeholder?: string;
  label?: string;
  max?: string,
  min?: string,
}>();
const emits = defineEmits<{
  (event: "update:modelValue", modelValue: string): void;
  (event: "input", modelValue: string): void;
  (event: "change", modelValue: string): void;
}>();

const onChange = ($event: Event) => {
  const value = ($event.target as HTMLInputElement).value;
  const currentVal = value
    .replace("-", "")
    .replace(".", "")
    .replace("e", "")
  emits('update:modelValue', currentVal)
  emits('change', currentVal)
}

const onInput = ($event: Event) => {
  const value = ($event.target as HTMLInputElement).value;
  const currentVal = value
    .replace("-", "")
    .replace(".", "")
    .replace("e", "")
  emits('update:modelValue', currentVal)
  emits('input', currentVal)
}

</script>

<template>
  <div class="ui-input">
    <label v-if="label">{{label}}</label>
    <div class="ui-input__wrapper">
      <input
        :value="modelValue"
        type="number"
        :max="max"
        :min="min"
        @input="onInput"
        @change="onChange"
      />
    </div>
  </div>
</template>

<style scoped lang="scss">
.ui-input {
  &__wrapper {
    padding: 4px;
    border-radius: 6px;
    border: 1px solid #2c3e50;
    min-width: 200px;
    & input {
      font-size: 14px;
      background: transparent;
      border: none;
      outline: none;
      width: 100%;
      -moz-appearance: textfield;
      &::-webkit-outer-spin-button,
      &::-webkit-inner-spin-button {
          -webkit-appearance: none;
          margin: 0;
        }
      }
    }
  }
</style>