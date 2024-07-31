import streamlit as st 
from math import asin, pi

L = st.number_input('Длина конуса')

D = st.number_input('Больший диаметр')
d = st.number_input('Меньший диаметр')

def calculate(L, D, d):
    if d > D:
        return 'Меньший диаметр не может быть больше большего'
    a = (D-d)/2
    c = (a**2+L**2)**.5
    try:
        corner = asin(a/c)*180/pi
    except ZeroDivisionError:
        return 'Размер 0 недопустим'
     
    return corner

with st.form('myform'):
    button = st.form_submit_button(label='Посчитать угол')
    if button:
        ans = calculate(L, D, d)
        if isinstance(ans, float):
            st.write(f'Угол составит {round(ans, 3)} градусов')
        else:
            st.write(ans)