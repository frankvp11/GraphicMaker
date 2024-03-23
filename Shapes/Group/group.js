export default {
    template: `
        <g ref='group' :transform="transform">
            <slot></slot>
        </g>
    `,
    props: {
        x: {
            type: Number,
            default: 0
        },
        y: {
            type: Number,
            default: 0
        },
    },
    computed: {
        transform() {
            return `translate(${this.x},${this.y})`;
        }
    }
};
