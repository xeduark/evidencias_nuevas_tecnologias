import streamlit as st
import pandas as pd
import io
import os

st.set_page_config(layout="wide")

st.subheader("Análisis y Filtrado de Datos")

actividad_1, actividad_2, actividad_3 = st.tabs(["Actividad#1", "Actividad#2", "Actividad#3"])

#----------------------------------------------------------
# Actividad 1
#----------------------------------------------------------
with actividad_1:      
    def mostrar_analisis_csv():
        st.title("Actividad 1 - semana 9")
        
        try:
            df = pd.read_csv('dat/demograficos.csv')
            st.subheader("Primeras 5 filas del DataFrame")
            st.dataframe(df.head())
            
            st.subheader("Información general del DataFrame")
            buffer = io.StringIO()
            df.info(buf=buffer)
            info_str = buffer.getvalue()
            st.text_area("Info del DataFrame", info_str, height=200)
            
            st.subheader("Estadísticas descriptivas")
            st.dataframe(df.describe())
            
            st.subheader("Valores únicos de la columna 'País'")
            paises_unicos = df["País"].unique()
            st.write(paises_unicos)
            
            st.subheader("Conteo de ocurrencias en la columna 'Género'")
            conteo_genero = df["Género"].value_counts()
            st.bar_chart(conteo_genero)
        except FileNotFoundError:
            st.error("Error: archivo 'datos_demograficos.csv' no encontrado.")

    mostrar_analisis_csv()

#----------------------------------------------------------
# Actividad 2
#----------------------------------------------------------
with actividad_2:    
    def mostrar_analisis_csv2():
        st.title("Actividad 2 - semana 9")

        try:
            df = pd.read_csv('dat/ventas.csv')
            st.subheader("Primeras 5 filas del DataFrame")
            st.dataframe(df.head())

            st.subheader("Filas con índices 5 a 10")
            filas_seleccionadas = df.iloc[5:11]
            st.dataframe(filas_seleccionadas)

            st.subheader("Columnas 'Producto' y 'Precio'")
            columnas_seleccionadas = df[['Producto', 'Precio']]
            st.dataframe(columnas_seleccionadas)

            st.subheader("Filas con 'Precio' mayor que 100")
            filtro_precio = df[df['Precio'] > 100]
            st.dataframe(filtro_precio)

            st.subheader("Agregar columna 'Descuento' (10% del 'Precio')")
            df['Descuento'] = df['Precio'] * 0.10
            st.dataframe(df)

            st.subheader("Eliminar columna 'Descuento'")
            df = df.drop(columns=['Descuento'])
            st.dataframe(df)

            st.subheader("Información general del DataFrame")
            buffer = io.StringIO()
            df.info(buf=buffer)
            info_str = buffer.getvalue()
            st.text_area("Info del DataFrame", info_str, height=200)

            st.subheader("Estadísticas descriptivas")
            st.dataframe(df.describe())
        except FileNotFoundError:
            st.error("Error: archivo 'ventas.csv' no encontrado.")

    mostrar_analisis_csv2()

#----------------------------------------------------------
# Actividad 3
#----------------------------------------------------------
with actividad_3:
    def mostrar_analisis_csv3():
        st.title("Actividad 3 - semana 9")

        try:
            df = pd.read_csv('dat/educacion.csv')

            st.subheader("Primeras 5 filas del DataFrame")
            st.dataframe(df.head())

            st.subheader("Información general del DataFrame")
            buffer = io.StringIO()
            df.info(buf=buffer)
            info_str = buffer.getvalue()
            st.text_area("Info del DataFrame", info_str, height=200)

            st.subheader("Estadísticas descriptivas")
            st.dataframe(df.describe())

            st.subheader("Niveles educativos más comunes")
            niveles_educativos = df['Nivel_Educativo'].value_counts()
            st.bar_chart(niveles_educativos)

            st.subheader("Carrera más popular")
            carrera_popular = df['Carrera'].value_counts().idxmax()
            st.write(f"La carrera más popular es: {carrera_popular}")

            st.subheader("Institución con más estudiantes")
            institucion_popular = df['Institución'].value_counts().idxmax()
            st.write(f"La institución con más estudiantes es: {institucion_popular}")

            st.subheader("Estudiantes con nivel educativo de posgrado")
            df_posgrado = df[df['Nivel_Educativo'] == 'Posgrado']
            st.dataframe(df_posgrado)

            st.subheader("Estudiantes de Ingeniería Informática en la Universidad Complutense de Madrid")
            df_ingenieria_madrid = df[(df['Carrera'] == 'Ingeniería Informática') & 
                                  (df['Institución'] == 'Universidad Complutense de Madrid')]
            st.dataframe(df_ingenieria_madrid)

            st.subheader("Estudiantes de Honduras con nivel universitario")
            df_honduras_universitario = df[(df['País'] == 'Honduras') & 
                                       (df['Nivel_Educativo'] == 'Universitario')]
            st.dataframe(df_honduras_universitario)

            st.subheader("Tabla de frecuencia por país y nivel educativo")
            tabla_frecuencia = pd.crosstab(df['País'], df['Nivel_Educativo'])
            st.dataframe(tabla_frecuencia)

            st.subheader("Edad promedio por nivel educativo")
            edad_promedio = df.groupby('Nivel_Educativo')['Edad'].mean()
            st.write(edad_promedio)

            df_posgrado.to_csv('dat/posgrado.csv', index=False)
            st.write("El DataFrame filtrado de posgrado se ha guardado en 'dat/posgrado.csv'")
        except FileNotFoundError:
            st.error("Error: archivo 'educacion.csv' no encontrado.")

    mostrar_analisis_csv3()
