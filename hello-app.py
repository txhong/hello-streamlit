import streamlit as st
import mymodel as m

st.write("""
# My first app
Hello *world!*""")

st.write(m.run(window=15))
