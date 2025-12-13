from capaLogicaNegocios.nPersona import NPersona
import streamlit as st

class PPersona:
    def __init__(self):
        self.__nPersona = NPersona()
        if 'formularioKey' not in st.session_state:
            st.session_state.formularioKey = 0
        self.__construirInterfaz()

    def __construirInterfaz(self):
        st.title('Registro usuario')
        if st.session_state.usuario_seleccionado != '':
            st.session_state.nombre_sesion = st.session_state.usuario_seleccionado['Nombre']
            st.session_state.apellido_sesion = st.session_state.usuario_seleccionado['Apellido']
            st.session_state.correo_sesion = st.session_state.usuario_seleccionado['Correo']
            st.session_state.contrasena_sesion = st.session_state.usuario_seleccionado['Contrasena']
        with st.form(f'Formulario {st.session_state.formularioKey}'):
            txtNombre = st.text_input('Nombre', value=st.session_state.nombre_sesion)
            txtApellido = st.text_input('Apellido', value=st.session_state.apellido_sesion )
            txtCorreo= st.text_input('Correo', value=st.session_state.correo_sesion)
            txtContrasena= st.text_input('Contrasena', value=st.session_state.contrasena_sesion)
            btnGuardar = st.form_submit_button('Guardar', type ='primary')

            if btnGuardar:
                usuario = {
                    'nombre': txtNombre,
                    'apellido': txtApellido,
                    'correo': txtCorreo,
                    'contrasena': txtContrasena
                }
                self.nuevaPersona(usuario)
        self.mostrarPersonas()

    def mostrarPersonas(self):
        listaPersonas = self.__nPersona.mostrarPersonas()
        col1, col2 = st.columns({10,2})
        with col1:
            usuario_seleccionado = st.dataframe(listaPersonas, selection_mode='single-row', on_select='rerun')
        with col2:
            if usuario_seleccionado.selection.rows:
                st.button('Editar')

    def nuevaPersona(self, usuario:dict):
        try:
            self.__nPersona.nuevaPersona(usuario)
            st.toast('Registro insertado', duration='short')
            self.limpiar()
        except Exception as e:
            st.error(e)
            st.toast('Registro no insertado', duration='short')

    def limpiar(self):
        st.session_state.formularioKey += 1
        st.rerun()

      