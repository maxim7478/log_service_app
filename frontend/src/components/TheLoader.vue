<script setup lang="ts">
import { onMounted } from 'vue'
import { gsap } from 'gsap'

onMounted(() => {
  const tLoader = gsap.timeline()
  tLoader
    .set('.loader__item', { yPercent: -100 })
    .set('.loader__title', { opacity: 0 })
    .to('.loader__item', {
      yPercent: 0,
      duration: 0.5,
      stagger: 0.25,
    })
    .to('.loader__item', {
      yPercent: 100,
      duration: 0.5,
      stagger: 0.25,
    })
    .to('.loader__title', {
      opacity: 1,
      duration: 1,
      scale: 1.2,
    })
    .set('.loader__item', {
      yPercent: -100,
    })
    .to('.loader__title', {
      opacity: 0,
      duration: 1,
      scale: 0.8,
    })
    .to('.loader', {
      yPercent: -100,
      duration: 1,
    }, '-=0.2')
})
</script>

<template>
  <div class="loader">
    <h1 class="loader__title">Welcome to Logs App</h1>
    <div class="loader__item"></div>
    <div class="loader__item"></div>
    <div class="loader__item"></div>
  </div>
</template>

<style scoped lang="scss">
.loader {
  height: 100%;
  width: 100%;
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  background: white;
  z-index: 1;
  &__title {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
  }
  &__item {
    flex: 1 1 auto;
    background: #2c3e50;
  }
}
</style>