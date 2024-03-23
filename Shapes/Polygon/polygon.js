export default {
  template: `
    <polygon ref='svg' :points="points" :fill="fill" pointer-events="all" />
  `,
  props: {
    points: { type: String, default: "100,10 40,198 190,78 10,78 160,198" }, 
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
