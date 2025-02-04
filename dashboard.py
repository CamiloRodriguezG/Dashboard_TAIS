import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Proceso ETL - Mercado libre")

# Cargar datos de cada pregunta
archivo_q1 = "feature_importances.csv"
archivo_q2 = "genres.csv"
archivo_q3 = ""
archivo_q4 = ""
archivo_q5 = ""  

# Función para cargar datos
def cargar_datos(archivo):
    try:
        return pd.read_csv(archivo)
    except Exception as e:
        st.error(f"Error al cargar el archivo CSV: {e}")
        return None

# Cargar los datos
q1 = {
    'pregunta': '¿Que tipo de productos son los que mas se devuelven por ubicacion geografica?',
    'datos': cargar_datos(archivo_q1)
}
q2 = {
    'pregunta': '¿Qué géneros de películas y series serán más consumidas en Mercado Play en diciembre - enero 2025?',
    'datos': cargar_datos(archivo_q2)
}
q3 = {
    'pregunta': '¿Qué productos de supermercado serán más consumidos en semana santa 2025?',
    # 'datos': cargar_datos(archivo_q3)
}
q4 = {
    'pregunta': '¿Qué licores serán los más consumidos en el periodo noviembre - enero 2025?',
    # 'datos': cargar_datos(archivo_q4)
}
q5 = {
    'pregunta': '¿Qué características de la publicación tuvieron un mayor impacto en el factor de conversión visita-ventas en productos de tecnología?',
    # 'datos': cargar_datos(archivo_q5)
}

# PREGUNTA 1
if q1 is not None:
    # Mostrar los datos en una tabla
    st.write(f'### {q1['pregunta']}')
    st.write(q1['datos'])
    
    # Gráfico de barras interactivo con Plotly (opcional)
    st.write("# Gráfico de barras")
    fig = px.bar(q1['datos'], x="Feature", y="Importance", 
                title="Importancia de características")
    st.plotly_chart(fig)
else:
    st.warning("No se pudieron cargar los datos. Verifica el archivo CSV.")

# PREGUNTA 2
if q2 is not None:
    # Mostrar los datos en una tabla
    st.write(f'### {q2['pregunta']}')
    st.write(q2['datos'])
    
    # Gráfico de barras interactivo con Plotly (opcional)
    st.write("# Gráfico de barras")
    fig = px.bar(q2['datos'], x="Genre", y="Importance", 
                title="Generos de peliculas por relevancia")
    st.plotly_chart(fig)
else:
    st.warning("No se pudieron cargar los datos. Verifica el archivo CSV.")
