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

    client = boto3.client('textract', region_name='us-west-1')

    response = client.analyze_document(
        Document={"Bytes": content},
        FeatureTypes=["TABLES", "FORMS"]
    )

    blocks = response["Blocks"]
    # width, height = image.size

    text = ''
    for block in response['Blocks']:
        if block['BlockType'].startswith("LINE"):
            text += block['Text']

    st.download_button(
        label="Download transcipt",
        data=text
    )

    st.write(text)


