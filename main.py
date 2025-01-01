import streamlit as st 
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


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

def generate_resturant_name_and_items(cuisine):
    llm=ChatGroq(
    model_name="llama-3.1-70b-versatile",
    groq_api_key="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",
    temperature=0.5,
    )

    prompt_temp=PromptTemplate(
    input_variables=['cusine'],
    template="I want to open a {cusine} resturant. Suggest some fancy name for it. Give only 1 name without any explaination or description."
    )
    
    name_chain=LLMChain(llm=llm,prompt=prompt_temp, output_key="resturant_name")
    
    prompt_temp_items=PromptTemplate(
    input_variables=['resturant_name'],
    template="Suggest some menu items for {resturant_name}. Return it as comma separated list"
    )

    menu_chain=LLMChain(llm=llm,prompt=prompt_temp_items, output_key="menu_items")


    chain=SequentialChain(
    chains=[name_chain,menu_chain], 
    input_variables=["cusine"],
    output_variables=["resturant_name","menu_items"]
    )   

    res=chain({"cusine":cuisine})
    #print(res)   

    return res


if cuisine:
    res = generate_resturant_name_and_items(cuisine)
    #print(res)

    st.header(f"Resturant Name: {res['resturant_name']}")
    st.write(f"Cuisine Chosen: {res['cusine']}")
    menu_items = res['menu_items'].split(',')
    st.header("**Menu Items:**")
    for item in menu_items:
        st.write(f"- {item.strip()}")


