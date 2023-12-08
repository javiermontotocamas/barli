<script>
export default {
    props: {
        title: String,
        value: String,
        type: String,
        active: Boolean
    },
    data() {
        return {
            editando: false,
            nuevoValor: ""
        };
    },
    watch: {
        active(newValue) {
            // Si el componente se activa, iniciar la edición
            if (newValue) {
                this.editando = true;
                this.nuevoValor = this.value;
            }
        }
    },
    methods: {
        alternarEdicion() {
            // Emitir evento para activar/desactivar el componente en el componente principal
            this.$emit("activate", !this.active);
            // Alternar el modo de edición solo si el componente está activo
            if (this.active) {
                this.editando = !this.editando;
                this.nuevoValor = this.value;
            }
        },
        guardarCambios() {
            this.$emit("change", this.nuevoValor);
            this.editando = false;
            this.nuevoValor = "";
        }
    }
};
</script>
<template>
    <div class="row">
        <div class="col-12 border border-dark">
            <p class="text-center p-3" @click="alternarEdicion"
                :style="{ cursor: 'pointer', color: active ? 'blue' : 'black' }">{{ title }}</p>
            <form v-if="active && editando" @submit.prevent="guardarCambios">
                <component :is="type === 'textarea' ? 'textarea' : 'input'" v-model="nuevoValor"
                    :class="{ 'form-control': type !== 'textarea' }" />
                <button type="submit" class="btn btn-primary">Guardar</button>
            </form>
        </div>
    </div>
</template>
<style scoped>
/* Agrega estilos según sea necesario */
</style>