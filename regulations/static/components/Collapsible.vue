<template>
    <div
        ref="target"
        v-bind:data-test="name"
        v-bind:class="{ invisible: !visible }"
        v-bind:style="[styles, sizeStyle]"
    >
        <slot></slot>
    </div>
</template>

<script>
export default {
    name: "collapsible",

    created: function () {
        requestAnimationFrame(() => {
            this.visible = this.state === "expanded";
            if (!this.visible) {
                this.$refs.target.classList.add("display-none");
            }
        });
        this.$root.$on("collapse-toggle", this.toggle);
    },

    mounted: function () {
        window.addEventListener("resize", this.resize);
        window.addEventListener("transitionend", this.toggleDisplay);
    },

    destroyed: function () {
        window.removeEventListener("resize", this.resize);
        window.removeEventListener("transitionend", this.toggleDisplay);
    },

    props: {
        name: {
            type: String,
            required: true,
        },
        state: {
            //expanded or collapsed
            type: String,
            required: true,
        },
        transition: {
            type: String,
            required: false,
            default: "0.5s",
        },
    },

    data: function () {
        return {
            name: this.name,
            height: "auto",
            visible: false,
            styles: {
                overflow: "hidden",
                transition: this.transition,
            },
        };
    },

    computed: {
        heightStyle: function () {
            return { height: this.height }
        },
    },

    methods: {
        resize: function (e) {
            this.computeHeight();
        },
        toggleDisplay: function (e) {
            if (this.visible) {
                this.$refs.target.style.height = "auto";
            }
            else {
                this.$refs.target.classList.add("display-none");
            }
        },
        toggle: function (target) {
            if (this.name === target) {
                this.$refs.target.classList.remove("display-none");
                requestAnimationFrame(() => {
                    this.computeHeight();
                    requestAnimationFrame(() => {
                        this.visible = !this.visible;
                    });
                });
            }
        },
        getStyle: function () {
            return window.getComputedStyle(this.$refs.target);
        },
        setProps: function (visibility, display, position, height) {
            this.$refs.target.style.visibility = visibility;
            this.$refs.target.style.display = display;
            this.$refs.target.style.position = position;
            this.$refs.target.style.height = height;
        },
        _computeHeight: function () {
            if (this.getStyle().display === "none") {
                return "auto";
            }

            this.$refs.target.classList.remove("invisible");

            this.setProps("hidden", "block", "absolute", "auto");

            const height = this.getStyle().height;

            this.setProps(null, null, null, height);
            if (!this.visible) {
                this.$refs.target.classList.add("invisible");
            }
            return height;
        },
        computeHeight: function () {
            this.height = this._computeHeight();
        },
    },
};
</script>
