<script>
export default {
  emits: ['close-modal'],
  methods: {
    closeModal() {
      this.$emit('close-modal', true)
    }
  }
}
</script>

<template>
  <div class="modal d-block" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
      <div class="modal-content w-100">
        <div id="modalhead" class="modal-header bg-secondary">
          <div class="modal-title">
            <slot name="titulo"></slot>
          </div>
          <button type="button" class="close bg-danger" @click="closeModal" aria-label="Close">
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
#modalhead {
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
  color: aliceblue;
  font-size: larger;
}
</style>
