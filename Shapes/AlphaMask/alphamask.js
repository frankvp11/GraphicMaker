export default {
  template: `
    <mask id="alpha-mask">
      <slot name="maskShape"></slot>
    </mask>

    <g mask="url(#alpha-mask)">
      <slot name="maskedShape"></slot>
    </g>
  `,
};
