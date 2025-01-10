import streamlit as st

name = st.text_input("Enter your name")
fname = st.text_input("Enter your father name")
adr = st.text_area("Enter your address")
classdata = st.selectbox("select your class:", (10, 11, 12, 13, 14, 15))

button = st.button("Submit")
if button :
    st.markdown(f"""
    Name : {name}\n
    Father Name: {fname}\n
    Address : {adr}\n
    Class : {classdata}\n
            """)