<template>
  <NuxtLayout name="default">
    <NuxtPage />
  </NuxtLayout>
</template>

<script setup>
import {
  initAccordions,
  initCarousels,
  initCollapses,
  initDials,
  initDismisses,
  initDrawers,
  initDropdowns,
  initModals,
  initPopovers,
  initTabs,
  initTooltips
} from "flowbite"

// initialize components based on data attribute selectors
onMounted(() => {
  initDismisses()
  initModals()
  initPopovers()
  initTooltips()
})
</script>
