import streamlit as st 
from math import asin, pi

L = st.number_input('Длина конуса')

D = st.number_input('Больший диаметр')
d = st.number_input('Меньший диаметр')

def calculate(L, D, d):
    if d > D:
        return 'Маленький диаметр не может быть больше большого'
    a = (D-d)/2
    c = (a**2+L**2)**.5
    corner = asin(a/c)*180/pi 
    return corner

with st.form('myform'):
    button = st.form_submit_button(label='Посчитать угол')
    if button:
        ans = round(calculate(L, D, d),3)
        st.write(f'Угол составит {ans} градусов')