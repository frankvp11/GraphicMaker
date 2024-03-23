export default {
  template: `
    <clipPath id="cut-off-bottom">
       <slot name="maskShape"></slot>
    </clipPath>

    <slot name="maskedShape" >  </slot>
  `,
};
    // "<circle cx='50' cy='50' r='50' fill='red' />"
