import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from streamlit_option_menu import option_menu
from streamlit_folium import st_folium
import folium

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
    
# Map Function

excel_file = pd.read_excel('data/Datasets.xlsx')
excel_file = excel_file.values

city = st.text_input("Enter your city name:")

if city:
    for business in excel_file:
        if business[2] == city:
            location = [business[5],business[6]]
            name = business[0]
            address = business[1]
            description = business[7]
            m = folium.Map(location=location, zoom_start=16)
            folium.Marker(
            [30.28799881847302, -97.72764340191415],
                popup=name,
                tooltip=address
            ).add_to(m)
            
            st_data = st_folium(m, width=725)
            st.write("Name: " + name)
            st.write("Address: " + address)
            st.write("Specialties: " + description)
            break

else:
    st.write("Enter your city name to get started.")
            
