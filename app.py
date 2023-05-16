import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

rand = np.random.normal(1,2,size=20)
fig,ax=plt.subplots0
ax.hist(rand,bins = 15)
st.pyplot(fig)


x = st.slider('Select a value')
st.write(x,'squared is',x * x)

st.sidebar.title("This is written inside th sidebar")
st.sidebar.button("Click")
st.sidebar.radio("Pick your gender",["Male","Female"])

st.number_input('Pick a number',0,10)
st.text_input('Email adress')
st.date_input('Travelling date')
st.time_input('school time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favouriote color')
