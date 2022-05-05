from google.cloud import vision
import streamlit as st

def detect_text(content):
    client = vision.ImageAnnotatorClient()

    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)

    header_text = """<h3 style="font-family: Monaco">Google</h3>"""
    st.markdown(header_text, unsafe_allow_html=True)
    st.download_button(
        label="Download transcipt",
        data='\n'.join([row.description for row in response.text_annotations])
    )

    image_col, text_col = st.columns(2)

    with image_col:
        st.image(content)

    with text_col:
        for page in response.full_text_annotation.pages:
            for block in page.blocks:
                st.write(f"Block confidence: {block.confidence}")
                for paragraph in block.paragraphs:
                    st.write(f"Paragraph confidence: {paragraph.confidence}")
                    for word in paragraph.words:
                        word_text = ''.join([symbol.text for symbol in word.symbols])
                        st.write(f"Word text: {word_text} (confidence: {word.confidence}")
