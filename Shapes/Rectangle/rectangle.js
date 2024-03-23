export default {
  template: `
    <rect ref='svg' :x="x" :y="y" :width="width" :height="height" :fill="fill" pointer-events="all" />
  `,
  props: {
    x: { type: Number, default: 75 },
    y: { type: Number, default: 75 },
    width: { type: Number, default: 50 },
    height: { type: Number, default: 50 },
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
};
