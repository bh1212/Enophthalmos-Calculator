import streamlit as st
import pandas as pd
import math 


col1, col2, col3,col4,col5,col6 = st.columns([1,1,5,3,1,1])

with col3:
    st.text('')
    st.image("R Adams Shock Trauma.png") 
with col4:
    st.image("JH logo.jpg")

st.header('')

st.markdown("<h4 style='text-align: center;'>Risk calculator for the prediction of postoperative enophthalmos following orbital fracture repair in adults</h4>", unsafe_allow_html=True)
#st.header("Risk calculator for the prediction of postoperative enophthalmos")

st.header('')
st.write('**Age at injury (≥18)**')
age_input = st.number_input('Select one of the following', 18, 150)
#st.text("")
st.write('**Preoperative enophthalmos:**')
yes_box = st.checkbox('Present',key = 1)
#st.text("")
st.write('**Fracture of medial wall:**')
present_box = st.checkbox('Present', key =2)
#st.text("")
st.write('**Near-total orbital floor defect:**')
yes2_box = st.checkbox('Present')
st.write('**Duration from injury to surgery:**')
duration_options = ['≤7 days', '8-14 days', '15-30 days', '>30 days']
selected_duration = st.selectbox('Select duration:', duration_options)




calculation = age_input * 0.036

if yes_box:
        calculation += 1 * 0.816

if present_box:
        calculation += 1 * 1.101

# Use the selected duration to adjust the calculation
if selected_duration == '≤7 days':
    calculation += 1 * 0
elif selected_duration == '8-14 days':
    calculation += 1 * 1.283
elif selected_duration == '15-30 days':
    calculation += 1 * 2.187
elif selected_duration == '>30 days':
    calculation += 1 * 2.45

if yes2_box:
        calculation += 1 * 0.597

calculation += (-6.844)


result = math.exp(calculation) / (math.exp(calculation) + 1) * 100

st.subheader('')

st.markdown(f"<h4>Risk (%) of postoperative enophthalmos = <span style='color:red'>{result:.2f}%</span></h4>", unsafe_allow_html=True)








