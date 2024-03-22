export default {
  template: `
    <circle ref='svg' :cx="cx" :cy="cy" :r="r" fill="black" pointer-events="all" />
  `,
  props: {
    cx: { type: Number, default: 100 },
    cy: { type: Number, default: 100 },
    r: { type: Number, default: 10 },
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
    handleMouseOver(event) {
      // Emitting mouseover event with event data
      console.log("Mouse over event", event);
      this.$emit("mouseover", event);
    },
    handleMouseOut(event) {
      // Emitting mouseout event with event data
      console.log("Mouse out event", event);
      this.$emit("mouseout", event);
    },
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
