export default {
  template: `
    <line ref='svg' :x1="x1" :y1="y1" :x2="x2" :y2="y2" :stroke="stroke" :stroke-width="stroke_width" :transform="svgTransform" pointer-events="all" />
  `,
  props: {
    x1: { type: Number, default: 10 },
    y1: { type: Number, default: 10 },
    x2: { type: Number, default: 190 },
    y2: { type: Number, default: 190 },
    stroke: { type: String, default: "black" },
    stroke_width: { type: Number, default: 1 },
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
