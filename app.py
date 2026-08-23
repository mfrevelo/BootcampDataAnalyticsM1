import streamlit as st

st.title("Bootcamp Data Analytics for Oil & Gas M1")
st.sidebar.title("Parameters")

modulos = st.sidebar.selectbox("Seleccione un modulo", ["Introduccion a variables", "Funciones","POO"])

if modulos == "Introduccion a variables":

    pozo = "SPE-001"
    petroleo_bpd = 1250
    agua_bpd = 350.50
    status = True
    liquido_total_bpd = petroleo_bpd + agua_bpd
    corte_agua_pct = agua_bpd / liquido_total_bpd * 100
    
    st.write("Pozo:", pozo)
    st.write("Petróleo (BPD):", petroleo_bpd)
    st.write("Agua (BPD):", agua_bpd)
    st.write("Estado Activo:", status)
    st.write("Líquido Total (BPD):", liquido_total_bpd)
    st.write("Corte de Agua (%):", corte_agua_pct)

elif modulos == "Funciones":
    
    def calcular_caudal_vogel(caudal_maximo=1200, presion_yacimiento=3000, presion_fondo=200, decimales=2):
        """
        Calculo de caudal de petroleo con Vogel
        
        Parámetros:
        caudal_maximo = Caudal maximo teorico del pozo, BPD
        presion_yacimiento = Presion promedio del pozo, PSI
        presion_fondo = Presion del fondo del pozo, PSI
        decimales = Cantidad de decimales que se quieren en el resultado
        """
        relacion_presion = presion_fondo / presion_yacimiento
        # Corrección: Se cambia caudal_max por caudal_maximo
        caudal = caudal_maximo * (1 - 0.2 * relacion_presion - 0.8 * (relacion_presion**2))
        return round(caudal, decimales)
    
    caudal_maximo = st.number_input("Ingrese el caudal maximo", min_value = 0, max_value = 5000, value = 1200)
    presion_yacimiento = st.number_input("Ingrese la presion de yacimiento", min_value = 0, max_value = 9000, value = 3000)
    presion_fondo = st.number_input("Ingrese la presion de fondo fluyente", min_value = 0, max_value = 9000, value = 1500)
    decimales = st.slider("Seleccione la cantidad de decimales para su resultado", min_value = 0, max_value = 4, value = 2)

    
    caudal = calcular_caudal_vogel(caudal_maximo, presion_yacimiento, presion_fondo, decimales)
    st.write("El caudal es:", caudal)
elif modulos == "POO":

    class Pozo:
      def __init__(self, nombre, campo, petroleo, agua):
    
        self.nombre = nombre
        self.campo = campo
        self.petroleo = petroleo
        self.agua = agua
    
      def mostrar_informacion(self):
        st.write("Nombre: ", self.nombre)
        st.write("Campo: ", self.campo)
        st.write("Petroleo: ", self.petroleo, "BPD")
        st.write("Agua: ", self.agua, "m3")
      
      def total_produccion(self):
        total_produccion = self.petroleo + self.agua
        return total_produccion
    
      def proyectar_produccion(self, dias):
        produccion_proyectada = (self.petroleo + self.agua) * dias
        return produccion_proyectada

    st.header("Ingreso de parametros: ")
    
    nombre_pozo = st.text_input("Ingrese el nombre del pozo: ")
    nombre_campo = st.text_input("Ingrese el campo al que pertenece el pozo: ")
    petroleo = st.number_input("Ingrese la produccion de petroleo", min_value = 0, max_value = 5000, value = 1200)
    agua = st.number_input("Ingrese la produccion de agua", min_value = 0, max_value = 5000, value = 1200)


    pozo = Pozo(nombre_pozo, nombre_campo, petroleo,agua)
    
    pozo.mostrar_informacion()
    st.write("Producción total:", pozo.total_produccion(), "BPD")
    dias = st.number_input("Ingrese los dias a proyectar: ", min_value = 0, max_value = 365)
    st.write(pozo.proyectar_produccion(dias))