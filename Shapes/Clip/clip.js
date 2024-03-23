export default {
  template: `
    <clipPath id="cut-off-bottom">
       <slot name="maskShape"></slot>
    </clipPath>
  <g clip-path="url(#cut-off-bottom)">
    <slot name="maskedShape"></slot>
  </g>
  
  `,
};
