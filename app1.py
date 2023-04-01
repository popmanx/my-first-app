import streamlit as st
from PIL import Image
IMG = Image.open("WhatsApp Image 2023-04-01 at 8.02.26 AM.jpeg")
IMG = IMG.resize((400,400))
st.sidebar.image(IMG)

IMG1 = Image.open("WhatsApp Image 2023-04-01 at 8.12.23 AM.jpeg")
IMG1 = IMG1.resize((300,300))
st.image(IMG1)


st.header("welcome to my first app")

st.text_input("what is your name")
st.number_input("what's your age", step = 1)
st.button("press me")
st.selectbox("gender",["Male", "Female","Others"])
st.checkbox("accept Teams and Conditions")
st.time_input("Select Time")
st.date_input("Sellect Date")
st.text_area("address")
st.sidebar.write("contact us")
st.sidebar.selectbox("menu",["emma","calab","popm"])
