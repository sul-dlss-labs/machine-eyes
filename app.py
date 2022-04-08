"""Machine Eyes Streamlit Application"""

import streamlit as st

st.title("Machine Eyes")
header_text = """<h3 style="color:#fe644e">Drop in a handwritten text pdf, jpg, png, or IIIF</h3>"""
st.markdown(header_text, unsafe_allow_html=True)

all_col, goog_col, ms_col, amz_col = st.columns(4)

with all_col:
    all_services = st.checkbox("All", key="all-services")

with goog_col:
    google = st.checkbox("Google", key="google", value=all_services)

with ms_col:
    microsoft = st.checkbox("Microsoft", key="microsoft", value=all_services)

with amz_col:
    amazon = st.checkbox("Amazon", key="amazon", value=all_services)

uploaded_file = st.file_uploader("", type=["pdf", "png", "jpg", "iiif"])

if uploaded_file:
    st.text("File uploaded")
