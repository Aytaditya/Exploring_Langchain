import streamlit as st 


st.set_page_config(layout="wide", page_title="Menu Generator", page_icon="🍔")

st.title("Resturant and Menu name Generator 🍔")
#st.write("This is a simple web app to generate resturant and menu names")
st.write("Please select a cuisine from the sidebar to generate a name of your resturant and its menu items will be generated for you")


# Sidebar, value chosen by user stored in cuisine variable
cuisine= st.sidebar.selectbox("Pick a cuisine",(
    "Italian",
    "Mexican",
    "American",
    "Chinese",
    "Indian",
    "Arabic",
    "Japanese",
    "Lebanese",
    "French",
))

#print(cuisine)

generate_resturant_name_and items(cuisine):

#if cuisine:
