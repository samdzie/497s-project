<template>
    <div id="calendar">
        <div id="margin">
            <span
                class="label"
                v-for="time in times"
                v-bind:key="time"
                v-bind:style="{ top: times.indexOf(time) * 40 + 30 + 'px' }"
            >
                {{ time }}
            </span>
        </div>
        <div class="column" v-for="day in days" v-bind:key="day">
            <div class="column-head">{{ day }}</div>
            <div
                class="column-body"
                v-bind:style="{ height: times.length * 40 + 'px'}"
            ></div>
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
            times: [
                '9 AM',
                '10 AM',
                '11 AM',
                '12 PM',
                '1 PM',
                '2 PM',
                '3 PM',
                '4 PM',
                '5 PM',
                '6 PM',
                '7 PM',
                '8 PM',
                '9 PM'
            ]
        };
    },
}
</script>

<style scoped>
#calendar {
    background-color: lightblue;
    display: flex;
    box-sizing: border-box;
    padding: 10px;
}
#margin, .column {
    position: relative;
    background-color: white;
}
#margin {
    width: 10%;
}
.column {
    width: calc(90% / 7);
    border-left: 1px solid lightgray;
}
.column-head {
    height: 20px;
    margin: 10px 0px;
    font-weight: bold;
}
.column-body {
    background: repeating-linear-gradient(
        to bottom,
        lightgray 0px 1px,
        white 1px 40px
    )
}
.label {
    position: absolute;
    right: 5px;
    line-height: 21px;
}
</style>
