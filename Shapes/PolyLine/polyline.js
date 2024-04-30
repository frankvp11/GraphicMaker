
export default {
    template: `
        <polyline ref='svg' :points="points" :fill="fill" :transform="svgTransform" pointer-events="all"  />
    `,
    props: {
        points: { type: String, default: "100,10 40,198 190,78 10,78 160,198" }, 
        fill: { type: String, default: "black" },
        x_scale_factor: { type: Number, default: 1 },
        y_scale_factor: { type: Number, default: 1 },
        rotate_angle: { type: Number, default: 0 },
        rotate_x: { type: Number, default: 0 },
        rotate_y: { type: Number, default: 0 },
        translate_x: { type: Number, default: 0 },
        translate_y: { type: Number, default: 0 },
        x_skew_factor: { type: Number, default: 0 },
        y_skew_factor: { type: Number, default: 0 },
    },
    computed: {
        svgTransform() {
        return `scale(${this.x_scale_factor}, ${this.y_scale_factor}) rotate(${this.rotate_angle},${this.rotate_x},${this.rotate_y}) translate(${this.translate_x}, ${this.translate_y}) skewX(${this.x_skew_factor}) skewY(${this.y_skew_factor})`;
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
        this.$refs.svg.addEventListener(event, (e) =>
            this.onPointerEvent(event, e)
        );
        }
    },
    methods: {
        onPointerEvent(event_type, event) {
        // Emitting pointer event with event data
        console.log("Pointer event", event);
        this.$emit(`svg:${event_type}`, {
            type: event_type,
            image_x: event.offsetX,
            image_y: event.offsetY 
        });
        },
    },
    };