export default {
  template: `
    <svg :viewBox="'0 0 ' + width + ' ' + height" :width="width" :height="height" xmlns="http://www.w3.org/2000/svg">
      <slot></slot>
    </svg>
  `,
  props: {
    width: { type: Number, default: 200 },
    height: { type: Number, default: 200 },
  },
};
