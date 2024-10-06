<script setup lang="ts">
interface IProps {
  theme?: 'primary' | 'second';
  isBorder?: boolean;
  isRound?: boolean;
}

withDefaults(defineProps<IProps>(), {
  theme: 'primary',
  isBorder: false,
  isRound: false
});
</script>

<template>
  <button :class="[
    'ui-button',
     `ui-button__${theme}`,
     { 'is-border': isBorder },
     { 'is-round': isRound },
  ]">
    <slot />
  </button>
</template>

<style scoped lang="scss">
.ui-button {
  padding: 8px;
  background: none;
  cursor: pointer;
  min-width: 100px;
  font-size: 14px;
  border: none;
  &__primary {
    color: white;
    background: #274D7E;
    transition: all 0.5s;
    &:hover {
      background: white;
      color: #274D7E;
      border-color: transparent;
    }
  }
  &__second {
    background: transparent;
    color: #274D7E;
    border-color: #274D7E;
    transition: all 0.5s;
    &:hover {
      color: white;
      background: #274D7E;
    }
  }
  &.is-border {
    border: 1px solid;
  }
  &.is-round {
    border-radius: 6px;
  }

}
</style>