export default {
  template: `
    <clipPath id="cut-off-bottom">
       <slot name="maskShape"></slot>
    </clipPath>

    <slot name="maskedShape" >  </slot>
  `,
};
