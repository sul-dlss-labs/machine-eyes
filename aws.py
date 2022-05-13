import io
import os
import sys

import boto3
import streamlit as st

from botocore.config import Config

from PIL import Image, ImageDraw

aws_access_key_id = os.environ['AWS_ACCESS_KEY']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

def _generate_annotated_image(content, blocks):
    image_stream = io.BytesIO(content)
    image = Image.open(image_stream)

    width, height = image.size

    for block in blocks:
        if block['BlockType'].startswith('LINE'):
            draw=ImageDraw.Draw(image)
            bounding_box = block['Geometry']['BoundingBox']
            left = width * bounding_box['Left']
            top = height * bounding_box['Top']

            rect = [
                left, 
                top, 
                left + (width * bounding_box['Width']),
                top + (height * bounding_box['Height'])
            ]

            draw.rectangle(
                 rect,
                 outline='red')

    return image


def aws_detect_text(content):

    header_text = """<h3 style="font-family: Monaco">Amazon</h3>"""
    st.markdown(header_text, unsafe_allow_html=True)

    client = boto3.client('textract',
        region_name='us-west-1',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    response = client.analyze_document(
        Document={"Bytes": content},
        FeatureTypes=["TABLES", "FORMS"]
    )

    blocks = response["Blocks"]

    text = []
    for block in blocks:
        if block['BlockType'].startswith("LINE"):
            text.append(block['Text'])

    st.download_button(
        label="Download transcipt",
        data='\n'.join(text)
    )

    image_col, text_col = st.columns(2)

    annotated_image = _generate_annotated_image(content, blocks)
    image_col.image(annotated_image)

    for row in text:
        text_col.write(row)


