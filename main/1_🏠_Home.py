import streamlit as st
from st_paywall import add_auth

st.set_page_config(
     page_title="Home", 
     page_icon=":house_with_garden:"
     )

st.markdown("# :turtle: Suscribete :turtle: ")

add_auth(required=True)

st.write(f"Suscription status : {st.session_state.user_subscribed}")
st.write("You´re all set and subscribed insert--emoji")
st.write(f"The email registered is {st.session_state.email}")
