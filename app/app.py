import base64
import streamlit as st
from lida import Manager, TextGenerationConfig, llm
from dotenv import load_dotenv
import os
import openai
from PIL import Image
from io import BytesIO
import tempfile  # For handling temporary files
import pandas as pd  # For handling CSV and Excel files

# Load environment variables and set the OpenAI API key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Create an instance of Manager class from lida library
lida = Manager(text_gen=llm("openai"))
textgen_config = TextGenerationConfig(
    n=1, temperature=0.5, model="gpt-3.5-turbo", use_cache=True
)

# Streamlit UI setup
menu = st.sidebar.selectbox("Choose an Option", ["Summarize", "Question based Graph"])

# Define a function to decode a base64 string to an image
def base64_to_image(base64_string):
    byte_data = base64.b64decode(base64_string)
    return Image.open(BytesIO(byte_data))

def handle_file_processing(uploaded_file):
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension in ['csv', 'xlsx']:
        if file_extension == 'csv':
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        # Save dataframe to a temporary file
        temp_path = os.path.join(tempfile.gettempdir(), uploaded_file.name)
        if file_extension == 'csv':
            df.to_csv(temp_path, index=False)
        else:
            df.to_excel(temp_path, index=False)
        
        return temp_path
    else:
        st.error("Unsupported file format.")
        return None


# Dedicated function for summarization
def summarize_data(file_path):
    summary = lida.summarize(
        file_path, summary_method="default", textgen_config=textgen_config
    )
    st.write(summary)

    goals = lida.goals(summary, n=2, textgen_config=textgen_config)
    for goal in goals:
        st.write(goal)

    charts = lida.visualize(
        summary=summary, goal=goals[0], textgen_config=textgen_config, library="seaborn"
    )
    if charts:
        img_base64_string = charts[0].raster
        img = base64_to_image(img_base64_string)
        st.image(img)
    else:
        st.write("No charts were generated.")

# Dedicated function for generating graphs based on user queries
def generate_query_based_graph(file_path, query):
    if not query:
        st.error("Please provide a query to generate the graph.")
        return
    
    st.info("Your Query: " + query)
    lida = Manager(text_gen = llm("openai")) 
    textgen_config = TextGenerationConfig(n=1, temperature=0.2, use_cache=True)
    summary = lida.summarize(file_path, summary_method="default", textgen_config=textgen_config)
    user_query = query
    charts = lida.visualize(summary=summary, goal=user_query, textgen_config=textgen_config)
    # charts[0]
    if charts:
        img_base64_string = charts[0].raster
        img = base64_to_image(img_base64_string)
        st.image(img)
    else:
        st.write("No charts generated.")


if menu == "Summarize":
    st.subheader("Summarization of your Data")
    file_uploader = st.file_uploader("Upload your CSV", type=["csv", "xlsx"])
    if file_uploader is not None:
        file_path = handle_file_processing(file_uploader)
        summarize_data(file_path)

# Choice for 'Question based Graph'
if menu == "Question based Graph":
    st.subheader("Query your Data to Generate Graph")
    file_uploader = st.file_uploader("Upload your CSV", type=["csv", "xlsx"])
    text_area = st.text_area("Enter your query here:", height=200)
    if st.button("Generate Graph") and file_uploader and text_area:
        file_path = handle_file_processing(file_uploader)
        generate_query_based_graph(file_path, text_area)
        os.remove(file_path)
