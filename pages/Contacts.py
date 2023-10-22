import streamlit as st
from PIL import Image

img = Image.open('logo.png')
st.set_page_config(page_title="Welfare for Workers", page_icon=img, layout="centered")

def app():
    st.write('Contacts')

st.write("Emails:")
st.write("Daniel Oake: droake2012@gmail.com")
st.write("Hieu Bui: hieubui0107@gmail.com")
st.write("Truc Le: trule4@my.lonestar.edu")