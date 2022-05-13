import io
import streamlit as st

from PIL import Image, ImageDraw
from google.cloud import vision


def _generate_annotated_image(content, annotations):
    image_stream = io.BytesIO(content)
    image = Image.open(image_stream)

    for word in annotations:
        bounding_poly = word.bounding_poly

        draw = ImageDraw.Draw(image)
        rect = [
            bounding_poly.vertices[0].x,  # left
            bounding_poly.vertices[0].y,  # top
            bounding_poly.vertices[-2].x,  # right
            bounding_poly.vertices[-2].y  # bottom  
        ]
        draw.rectangle(rect, outline='red')

    return image

def gcp_detect_text(content):
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


    annotated_image = _generate_annotated_image(content, response.text_annotations)

    with image_col:
        st.image(annotated_image)

    with text_col:
        for row in response.text_annotations:
            st.write(row.description)
