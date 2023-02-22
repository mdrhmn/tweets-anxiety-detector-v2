<template>
  <NuxtLayout name="default">
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup>
import {
  initDismisses,
  initModals,
  initPopovers,
  initTooltips,
} from "flowbite";

// initialize components based on data attribute selectors
onMounted(() => {
  initDismisses();
  initModals();
  initPopovers();
  initTooltips();
});
</script>
