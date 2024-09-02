import streamlit as st
st.title('My first app')
st.write('Hello all')
x=st.text_input('Which Technology you want to learn')
if x=='Ai':
    st.write('Kindly enroll in python first')
y=st.radio('Are you Graduate',options=['Yes','No'])
if y=='Yes':
    st.write('You can enroll in our diploma course')
else:
    st.write('You can do Internship ')
#a=st.button('Show')

z=st.selectbox('Select the Technology',('Python','Java','C++'))
if z=='Python':
    st.write('contact abc 98765457')
elif z=='Java':
    st.write('contact xyz 98765457')
elif z=='C++':
    st.write('contact pqr 98765457')

st.button('select from list given')