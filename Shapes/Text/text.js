export default {
    template: `
        <text ref='svg' :x="x" :y="y" :fill="fill" :font-size="font_size" :font-family="font_family" pointer-events="all">{{ text }}</text>
    `,
    props: {
        x: { type: Number, default: 10 },
        y: { type: Number, default: 10 },
        fill: { type: String, default: "black" },
        font_size: { type: Number, default: 16 },
        font_family: { type: String, default: "Arial" },
        text: { type: String, default: "Hello" },
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