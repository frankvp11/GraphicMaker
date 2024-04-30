export default {
  template: `
    <svg :viewBox="viewBox" :width="width" :height="height" xmlns="http://www.w3.org/2000/svg">
      <slot></slot>
    </svg>
  `,
  props: {
    width: { type: Number, default: 200 },
    height: { type: Number, default: 200 },
    viewBox: { type: String, default: "0 0 200 200" },
  },
};
