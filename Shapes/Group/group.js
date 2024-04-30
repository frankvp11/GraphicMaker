export default {
    template: `
        <g ref='group' :transform="transform" pointer-events="all">
            <slot></slot>
        </g>
    `,
    props: {
        x: {
            type: Number,
            default: 0
        },
        y: {
            type: Number,
            default: 0
        },
    },
    computed: {
        transform() {
            return `translate(${this.x},${this.y})`;
        }
    },

    mounted() {
        for (const event of [
        "pointermove",
        "pointerdown",
        "pointerup",
        "pointerover",
        "pointerout",
        "pointerenter",
        "pointerleave",
        "pointercancel",
        ]) {
        this.$refs.group.addEventListener(event, (e) =>
            this.onPointerEvent(event, e)
        );
        }
    },
    methods: {
        onPointerEvent(event_type, event) {
        // Emitting pointer event with event data
        console.log("Pointer event on group")
        this.$emit(`svg:${event_type}`, {
            type: event_type,
            image_x: event.offsetX,
            image_y: event.offsetY,
        });
        },
    },

};
