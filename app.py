import streamlit as st
from openai import OpenAI

st.balloons()
# Show title and description.
st.title("💬 Mi Asistente Robot")
st.write(
   "Hola, este es un robot asistente que funciona con un modelo GPT-3.5 para generar respuestas. "
   "Para utilizar este asistente, simplemente teclea tu pregunta [here](https://platform.openai.com/account/api-keys). "
   "En este enlace podrás aprender como diseñar tu robot paso a paso [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
)
openai_api_key = st.secrets["api_key"] 
# Create an OpenAI client.
client = OpenAI(api_key=openai_api_key)

prompt = st.chat_input("Estoy a la orden")
if prompt==None:
   st.stop()

with st.chat_message("user"):
   st.markdown(prompt)


# Generate a response using the OpenAI API.

stream = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "system", "content": "You are an assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=800,
        temperature=0,
    )
respuesta = stream.choices[0].message.content
with st.chat_message("assistant"):
   st.write(respuesta)
