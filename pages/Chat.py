import streamlit as st

def app():
    st.write('Home')

body = "<script src=\"https://cdn.botpress.cloud/webchat/v1/inject.js\"></script><script src=\"https://mediafiles.botpress.cloud/1ead3258-715f-4967-8e76-e4279e1f3c5b/webchat/config.js\" defer></script>

st.markdown(body, unsafe_allow_html= True)