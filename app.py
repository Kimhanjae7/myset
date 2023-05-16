import streamlit as st
import pandas as pd
import numpy as np
import graphviz as graphviz

x = st.slider('Select a value')
st.write(x,'squared is',x * x)

st.sidebar.title("This is written inside th sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Pick your gender",["Male","Female"])     

st.graphviz_chart('''
    digraph {
        Big_shark -> Tuna
        Tuna -> Mackerel
        Mackerel -> Small_fishes
        Small_fishes -> Shrimp
    }
''')
