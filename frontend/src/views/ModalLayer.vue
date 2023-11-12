<script>
export default {
    methods: {
        closeModal() {
            this.$emit('close-modal', true);
        }
    }
}
</script>

<template>
    <!--div class="modal fade show" tabindex="-1" role="dialog">-->
    <div>
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <div class="modal-title">
                        <slot name="titulo"></slot>
                    </div>
                    <button type="button" class="close" @click="closeModal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <slot name="cuerpo"></slot>
                </div>
                <div class="modal-footer">
                    <slot name="pie"></slot>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>