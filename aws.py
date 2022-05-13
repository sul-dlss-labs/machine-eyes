import os
import sys

import boto3
import streamlit as st

from botocore.config import Config

from PIL import Image, ImageDraw, ImageFont

aws_access_key_id = os.environ['AWS_ACCESS_KEY']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

def aws_detect_text(content):

    # image = Image()

    st.header("Amazon")

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
    
    image_col.image(content)

    for row in text:
        text_col.write(row)


