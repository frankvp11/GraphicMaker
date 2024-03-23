export default {
  template: `
    <rect ref='svg' :x="x" :y="y" :width="width" :height="height" :fill="fill" :stroke="outline_color" :stroke-width="outline_width" :transform="svgTransform" pointer-events="all"  />
  `,
  props: {
    x: { type: Number, default: 75 },
    y: { type: Number, default: 75 },
    width: { type: Number, default: 50 },
    height: { type: Number, default: 50 },
    fill: { type: String, default: "black" },
    outline_color: { type: String, default: "black" },
    outline_width: { type: Number, default: 1 },
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
        image_y: event.offsetY,
      });
    },
  },
};
