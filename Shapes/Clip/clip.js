export default {
  template: `
    <mask>
      <slot name="maskShape"></slot>
    </mask>
    <g mask="url(#mask)">
      <slot name="maskedShape"></slot>
    </g>
  `,
};
