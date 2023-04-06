import openai
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_app import check_password


# Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = st.secrets["OPENAI_API_BASE"]
openai.api_version = "2023-03-15-preview"
openai.api_key = st.secrets["OPENAI_API_KEY"]

response = openai.ChatCompletion.create(
    engine="gpt-4",  # engine = "deployment_name".
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant",
            "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure Cognitive Services support this too?"}
    ]
)

print(response)
print(response['choices'][0]['message']['content'])
