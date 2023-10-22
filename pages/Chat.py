import streamlit as st

from PIL import Image

img = Image.open('logo.png')
st.set_page_config(page_title="Welfare for Workers", page_icon=img, layout="centered")

def app():
    st.write('Home')


link = '[Botpress](https://mediafiles.botpress.cloud/1ead3258-715f-4967-8e76-e4279e1f3c5b/webchat/bot.html)'

st.write(f"Link to Chaptbot {link}")

