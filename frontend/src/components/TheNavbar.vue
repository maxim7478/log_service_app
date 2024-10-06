<script setup lang="ts">
const navList = [
  {
    id: 1,
    title: 'Home',
    routeName: 'home',
  },
  {
    id: 2,
    title: 'Logs',
    routeName: 'logs',
  },
]
</script>

<template>
<div class="the-navbar">
  <div class="the-navbar__list">
    <router-link v-for="item in navList" :key="`navItems-${item.id}`" :to="{name: item.routeName}" class="the-navbar__item">
      {{ item.title }}
    </router-link>
  </div>
</div>
</template>

<style scoped lang="scss">
.the-navbar {
  background: #274D7E;
  padding: 20px;
  &__list {
    margin: 0 auto;
    max-width: 1280px;
    display: grid;
    list-style-type: none;
    gap: 10px;
    align-items: center;
    padding: 0;
  }
  &__item {
    color: white;
    text-decoration: none;
    cursor: pointer;
  }
  & .router-link-exact-active {
    color: #FF9E00;
  }
}
</style>