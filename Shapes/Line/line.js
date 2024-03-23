export default {
    template: `
        <line ref='svg' :x1="x1" :y1="y1" :x2="x2" :y2="y2" :stroke="stroke" :stroke-width="stroke_width" pointer-events="all" />
    `,
    props: {
        x1: { type: Number, default: 10 },
        y1: { type: Number, default: 10 },
        x2: { type: Number, default: 190 },
        y2: { type: Number, default: 190 },
        stroke: { type: String, default: "black" },
        stroke_width: { type: Number, default: 1 },
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
        this.$refs.svg.addEventListener(event, (e) =>
            this.onPointerEvent(event, e)
        );
        }
    },
    methods: {
    
        onPointerEvent(event_type, event) {
        // Emitting pointer event with event data
        const width = this.$refs.svg.clientWidth;
        const height = this.$refs.svg.clientHeight;
        console.log("Pointer event", event);
        this.$emit(`svg:${event_type}`, {
            type: event_type,
            image_x: (event.offsetX * width) / event.x,
            image_y: (event.offsetY * height) / event.x,
        });
        },
    },
};
