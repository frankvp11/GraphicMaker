export default {
    template: `
        <ellipse ref='svg' :cx="cx" :cy="cy" :rx="rx" :ry="ry" :fill="fill" pointer-events="all" clip-path="url(#cut-off-bottom)" />
    `,
    props: {
        cx: { type: Number, default: 100 },
        cy: { type: Number, default: 100 },
        rx: { type: Number, default: 50 },
        ry: { type: Number, default: 50 },
        fill: { type: String, default: "black" },
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
}