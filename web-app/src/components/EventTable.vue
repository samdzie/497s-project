<template>
    <table>
        <thead>
            <tr>
                <th>Event</th>
                <th>Start</th>
                <th>End</th>
            </tr>
        </thead>
        <tbody>
            <EventRow
                v-for="event in events"
                :key="event.id"
                v-bind:title="event.title"
                v-bind:start="event.start"
                v-bind:end="event.end"
            />
        </tbody>
    </table>
</template>

<script>
import EventRow from './EventRow.vue'

export default {
    name: 'EventTable',
    components: {
        EventRow
    },
    props: {
        someProp: String
    },
    data: function() {
        return {
            events: []
        };
    },
    beforeMount() {
        this.getEvents();
    },
    methods: {
        async getEvents() {
            const resp = await fetch('http://localhost:5000/api/events');
            const json = await resp.json();
            this.events = json.events.slice();
        }
    }
}
</script>

<style scoped>
table {
    background-color: bisque;
    width: 100%;
    border-radius: 5px;
}
th {
    padding: 5px;
}
</style>
