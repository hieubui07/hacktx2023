import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Welfare for Worker", page_icon=":tada:", layout="centered")

import home, projects, contacts
st.title("Home")

# HEADER SECTION 
with st.container():
    st.title('Wealthfare for Workers')
    st.text('Description')
    
with st.container():
    st.text('Search Bar')

with st.container():
    st.write("---------")
    left_column,right_column = st.columns(2)
    with left_column:
        st.header("Pics")
        st.write("##")
        st.write(
            "Searching for psychiatrists?"
        )
    with right_column:
        st.header('Address and name of psychiatrists')
        
class MultiApp:
    
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })
        
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title='Main Menu',
                options=['Home','Projects','Contacts'],
                icons=['house','book','phone'],
                menu_icon='chat-text-fill',
                default_index=1,
            
            )
            
            if app=='Home':
                home.app()
            if app=='Projects':
                projects.app()
            if app== 'Contacts':
                contacts.app()
    
    run()
                
        