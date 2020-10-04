<template>
    <EventTable />
</template>

<script>
import EventTable from './components/EventTable.vue'

export default {
    name: 'App',
    components: {
        EventTable
    }
}
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
    margin-left: auto;
    margin-right: auto;
    width: 800px;
}
</style>
