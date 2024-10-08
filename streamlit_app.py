import streamlit as st
from openai import OpenAI
import os

# Inyectar CSS en la aplicación
st.markdown("""
    <style>
    .stButton button {
        background-color:   #c5888a  ;
        color: white;
        font-size: 34px;
        height: 80px;
        width: 300px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Show title and description.
st.title("Planea tu próximo viaje")
st.image("caratula3.jpeg", use_column_width=True)

st.write(
    "Vamos a crear tu itinerario personalizado"
    " del viaje que deseas hacer"
)

# Parámetros del usuario
user_pais_input = st.text_input(label="Lugar", value="", key="hidden_input1", 
                                placeholder="Dime qué país, ciudad o área del mundo quieres visitar",
                                autocomplete = "on")

#user_pais_input = st.text_input("Lugar", "Dime qué país, ciudad o área del mundo quieres visitar",autocomplete = "on")
user_dias_input = st.text_input(label="Días", value="", key="hidden_input2",
                                placeholder="¿Cuántos días estarás?")
user_company_input = st.text_input(label="Gente",value="", key="hidden_input3",
                                placeholder="Cuéntame si viajarás solo, con pareja, con familia, en general con cuántas personas")
user_intereses_input = st.text_input(label="Intereses", value="", key="hidden_input5",
                                     placeholder="Cuéntame qué tipo de intereses tienes: comida, vida nocturna, montaña, etc.")
user_dinero_input = st.text_input(label="Dinero", value="", key="hidden_input6",
                                  placeholder="Cuéntame cuánto dinero estás pensando en gastar")
user_restricciones_input = st.text_input(label="Restricciones", value="", key="hidden_input4",
                                         placeholder="Cuéntame algo que no quieres para este viaje")

# Generar el prompt
prompt = f"""
Crea un itinerario detallado para {user_pais_input} por {user_dias_input} días.
El viaje será {user_company_input}.
las restricciones son: {user_restricciones_input}.
Los intereses del viaje: {user_intereses_input}.
El presupuesto para el viaje es de {user_dinero_input}.
¿Podrías crear un itinerario detallado para este viaje, que de ideas originales incluyendo actividades diarias, lugares que existan ahora recomendados para visitar y sugerencias de restaurantes con nombre que se ajusten al presupuesto?
Tambien al final podrias crear una seccion de 4 paginas webs que hablen de viajes a la {user_pais_input} dada
"""

# clave de openAI

openai_api_key = os.getenv('OPENAI_API_KEY')
# Generate a response using the OpenAI API.

def generar_itinerario(prompt,openai_api_key):
    client = OpenAI(api_key= openai_api_key)
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        temperature=0.7,
        messages = [{'role': 'user', 'content': prompt}]
        )
    return response.choices[0].message.content


# Botón para generar el itinerario
if st.button("Generar Itinerario"):
    if all([user_pais_input, user_dias_input, user_company_input, user_restricciones_input, user_intereses_input, user_dinero_input]):
        itinerario = generar_itinerario(prompt,openai_api_key)
        st.subheader("Itinerario de Viaje Generado:")
        st.write(itinerario)
    else:
        st.error("Por favor, completa todos los campos para generar el itinerario.")
