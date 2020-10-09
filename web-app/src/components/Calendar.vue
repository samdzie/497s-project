<template>
    <div id="calendar">
        <div id="margin">
            <div class="column-head"></div>
            <div
                class="time-chunk"
                v-for="chunk in chunks"
                v-bind:key="chunk"
            >
                {{ chunk }}
            </div>
        </div>
        <div class="column" v-for="day in days" v-bind:key="day">
            <div class="column-head">{{ day }}</div>
            <div
                class="time-chunk"
                v-for="chunk in chunks"
                v-bind:key="chunk"
            >
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Calendar',
    data() {
        return {
            days: [
                'Sunday',
                'Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday',
                'Saturday'
            ],
            chunks: [],
        };
    },
    beforeMount() {
        this.generateChunks();
    },
    methods: {
        generateChunks() {
            let chunks = [];
            const N = 24;
            for (let i = 0; i <= N; i++) {
                let hour = (i + 11) % 12 + 1;
                let chunk = (i < N / 2) ? hour + ':00 AM' : hour + ':00 PM';
                chunks.push(chunk);
            }
            this.chunks = chunks;
        },
    }
}
</script>

<style scoped>
#calendar {
    --time-chunk-height: 30px;
    background-color: lightblue;
    display: flex;
    box-sizing: border-box;
    padding: 10px;
}
#margin, .column {
    border: 1px solid black;
}
#margin {
    width: 10%;
}
.column {
    width: calc(90% / 7);
    border-left: none;
}
.column-head {
    height: 20px;
    margin: 10px 0px;
    font-weight: bold;
}
.time-chunk {
    height: var(--time-chunk-height);
    border-top: 1px solid black;
    line-height: var(--time-chunk-height);
}
</style>
