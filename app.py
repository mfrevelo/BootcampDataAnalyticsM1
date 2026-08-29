import streamlit as st
import pandas as pd

from funciones_calculos import (calcular_liquido, calcular_bsw, proyectar_produccion)

from funciones_datos import (filtrar_pozo,resumen_dataframe)

from clase_pozo import Pozo


st.title("Bootcamp Data Analytics for Oil & Gas")
st.sidebar.title("Parámetros")

modulos = st.sidebar.selectbox("Selecione un módulo", ["Introducción a variables", "Funciones","POO", "Importación de Librerias"])

if modulos == "Introducción a variables":

  pozo = "SPE-001"
  petroleo_bpd = 1250
  agua_bpd = 350.50
  status = True
  
  st.write(pozo)
  st.write(petroleo_bpd)
  st.write(agua_bpd)
  st.write(status)
elif  modulos == "Funciones": 
  
  def calcular_caudal_vogel(caudal_maximo=1000, presion_yacimiento=3000, presion_fondo=200, decimales=2):
    """
      Calcula el caudal de petróleo mediante la ecuación de Vogel.
  
      Parámetros:
      caudal_maximo (float): Caudal máximo teórico del pozo, BPD.
      presion_yacimiento (float): Presión promedio del yacimiento, psi.
      presion_fondo (float): Presión de fondo fluyente, psi.
      decimales (int): Número de decimales del resultado.
  
      Retorna:
      float: Caudal estimado de petróleo, BPD.  
    """
  
    relacion_presion = presion_fondo/presion_yacimiento
    caudal = caudal_maximo*( 1 -0.2*relacion_presion - 0.8*(relacion_presion**2))
    
    return round(caudal, decimales)

  caudal_maximo = st.number_input("Ingrese el caudal máximo", min_value = 0, max_value = 5000, value =1200)
  presion_yacimiento = st.number_input("Ingrese la presion del yacimiento",min_value = 0, max_value = 9000, value =3000)
  presion_fondo = st.number_input("Ingrese la presion de fondo fluyente",min_value = 0, max_value = 9000, value =1500)
  decimales = st.slider("Seleccione la cantidad de decimales para su resultado",min_value = 0, max_value = 4, value =2)

  caudal = calcular_caudal_vogel(caudal_maximo, presion_yacimiento, presion_fondo, decimales)

  st.write("El caudal es:", caudal)

elif  modulos == "POO": 

  class Pozo:
  
    def __init__(self,nombre, campo, petroleo, agua):
      self.nombre = nombre
      self.campo = campo
      self.petroleo = petroleo
      self.agua = agua
  
    def mostrar_informacion(self):
      st.write("Pozo:", self.nombre)
      st.write("Campo:", self.campo)
      st.write("Petroleo:", self.petroleo, "BPD")
      st.write("Agua:", self.agua, "BPD")
  
    def produccion_total(self):
      total_produccion = self.petroleo + self.agua
      return total_produccion
  
    def proyectar_produccion(self, dias=30):
      produccion_proyectada = (self.petroleo + self.agua)*dias
      return produccion_proyectada

  nombre_pozo = st.text_input("Ingrese el nombre del pozo")
  campo_pozo = st.text_input("Ingrese el campo al que pertenece el pozo")
  petroleo = st.number_input("Ingrese producción de petróleo", min_value = 0, max_value = 5000, value =1000)
  agua = st.number_input("Ingrese producción de agua", min_value = 0, max_value = 5000, value =200)

  pozo = Pozo(nombre_pozo,campo_pozo,petroleo,agua)

  st.write(pozo.mostrar_informacion())

  st.write(pozo.produccion_total())

  dias = st.number_input("Ingrese los días a proyectar", min_value = 0, max_value = 365, value =30)
  st.write(pozo.proyectar_produccion(dias))

elif  modulos == "Importación de Librerias": 
  st.title("Aplicación Modular con Funciones y Clases")
  st.header("1. Uso de funciones")
  
  petroleo = st.number_input(
    "Producción de petróleo",
    min_value=0.0,
    value=800.0)

  agua = st.number_input(
      "Producción de agua",
      min_value=0.0,
      value=200.0
  )

  dias = st.number_input(
      "Días",
      min_value=1,
      value=30
  )
  
  if st.button("Calcular"):
    liquido = calcular_liquido(
        petroleo,
        agua
    )

    bsw = calcular_bsw(
        petroleo,
        agua
    )

    proyeccion = proyectar_produccion(
        petroleo,
        dias
    )

    st.write("Producción líquida:", liquido)
    st.write("BSW:", round(bsw, 2), "%")
    st.write("Producción proyectada:", proyeccion)
