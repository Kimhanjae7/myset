import streamlit as st
import pandas as pd
import numpy as np
import graphviz as graphviz

x = st.slider('Select a value')
st.write(x,'squared is',x * x)

st.sidebar.title("This is written inside th sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Pick your gender",["Male","Female"])     
