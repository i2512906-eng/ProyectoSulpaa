from capaLogicaNegocios.nPersona import NPersona
import streamlit as st


class PPersona:
    def __init__(self):
        self.__nPersona = NPersona()

        if 'formularioKey' not in st.session_state:
            st.session_state.formularioKey = 0
        if 'usuario_seleccionado' not in st.session_state:
            st.session_state.usuario_seleccionado = None
        if 'nombre_sesion' not in st.session_state:
            st.session_state.nombre_sesion = ''
        if 'apellido_sesion' not in st.session_state:
            st.session_state.apellido_sesion = ''
        if 'correo_sesion' not in st.session_state:
            st.session_state.correo_sesion = ''
        if 'contrasena_sesion' not in st.session_state:
            st.session_state.contrasena_sesion = ''

        self.__construirInterfaz()

    def __construirInterfaz(self):
        st.title('Registro de usuarios')

        if st.session_state.usuario_seleccionado:
            st.session_state.nombre_sesion = st.session_state.usuario_seleccionado['nombre']
            st.session_state.apellido_sesion = st.session_state.usuario_seleccionado['apellido']
            st.session_state.correo_sesion = st.session_state.usuario_seleccionado['correo']
            st.session_state.contrasena_sesion = st.session_state.usuario_seleccionado['contrasena']

        with st.form(f'Formulario {st.session_state.formularioKey}'):
            txtNombre = st.text_input('Nombre', value=st.session_state.nombre_sesion)
            txtApellido = st.text_input('Apellido', value=st.session_state.apellido_sesion)
            txtCorreo = st.text_input('Correo', value=st.session_state.correo_sesion)
            txtContrasena = st.text_input('Contraseña', value=st.session_state.contrasena_sesion)

            if st.session_state.usuario_seleccionado:
                btnActualizar = st.form_submit_button('Actualizar')
                if btnActualizar:
                    usuario = {
                        'nombre': txtNombre,
                        'apellido': txtApellido,
                        'correo': txtCorreo,
                        'contrasena': txtContrasena
                    }
                    self.actualizarPersona(usuario, txtNombre)
            else:
                btnGuardar = st.form_submit_button('Guardar')
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

        if not listaPersonas:
            st.info('No hay usuarios registrados')
            return

        st.subheader('Usuarios registrados')
        st.dataframe(listaPersonas)

        opciones = [f"{u['nombre']} {u['apellido']}" for u in listaPersonas]
        seleccion = st.selectbox(
            'Selecciona un usuario',
            ['-- Seleccionar --'] + opciones
        )

        if seleccion != '-- Seleccionar --':
            indice = opciones.index(seleccion)
            usuarioSeleccionado = listaPersonas[indice]

            col1, col2 = st.columns(2)

            with col1:
                if st.button('Editar'):
                    st.session_state.usuario_seleccionado = usuarioSeleccionado
                    st.rerun()

            with col2:
                if st.button('Eliminar'):
                    self.eliminarPersona(usuarioSeleccionado['nombre'])
                    st.rerun()

    def nuevaPersona(self, usuario: dict):
        try:
            lista = self.__nPersona.mostrarPersonas()
            correos = [u['correo'] for u in lista]

            if usuario['correo'] in correos:
                st.warning('Ese correo ya está registrado')
                return

            self.__nPersona.nuevaPersona(usuario)
            st.success('Registro insertado')
            self.limpiar()

        except Exception as e:
            st.error(e)

    def actualizarPersona(self, usuario: dict, nombre: str):
        try:
            lista = self.__nPersona.mostrarPersonas()

            for u in lista:
                if u['correo'] == usuario['correo'] and u['nombre'] != nombre:
                    st.warning('Ese correo ya pertenece a otro usuario')
                    return

            self.__nPersona.actualizarPersona(usuario, nombre)
            st.success('Registro actualizado')
            self.limpiar()

        except Exception as e:
            st.error(e)

    def eliminarPersona(self, nombre: str):
        try:
            self.__nPersona.eliminarPersona(nombre)
            st.success('Registro eliminado')
        except Exception as e:
            st.error(e)

    def limpiar(self):
        st.session_state.formularioKey += 1
        st.session_state.usuario_seleccionado = None
        st.session_state.nombre_sesion = ''
        st.session_state.apellido_sesion = ''
        st.session_state.correo_sesion = ''
        st.session_state.contrasena_sesion = ''
        st.rerun()
