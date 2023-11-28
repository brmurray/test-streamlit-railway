import streamlit as st

# Title of the app
st.title('Simple Streamlit App')

# A button to greet the user
if st.button('Say hello'):
    st.write('Why hello there!')
else:
    st.write('Goodbye')
