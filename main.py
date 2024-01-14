import streamlit as st
import AI as ai

st.title("mini bard")

inp = st.sidebar.text_area(label="Ask any quesion", max_chars= 100)

if inp:
    response = ai.bard(inp)
    st.text(response)