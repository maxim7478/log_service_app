<script setup lang="ts">
import TheLoader from '@/components/TheLoader.vue'
import TheNavbar from '@/components/TheNavbar.vue'
</script>

<template>
  <the-loader />
  <router-view v-slot="{ Component }">
    <transition
      name="fade"
      mode="out-in"
    >
      <component :is="Component" />
    </transition>
  </router-view>
</template>

<style scoped lang="scss">
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease-out;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
