# import base64  # For encoding and decoding base64 strings.
# import streamlit as st  # A library for creating web applications with Python.
# from lida import (
#     Manager,
#     TextGenerationConfig,
#     llm,
# )  # A library for AI-assisted data analysis.
# from dotenv import load_dotenv  # For loading environment variables from a .env file
# import os  # Python library for OpenAI API.
# import openai
# from PIL import Image  # For working with images.
# from io import BytesIO  # For working with in-memory binary data.

# # Loads environment variables from a .env file and sets the OpenAI API key.
# load_dotenv()

# # Retrieve the OpenAI API key
# openai_api_key = os.getenv("OPENAI_API_KEY")


# # Defines a function 'base64_to_image' that decodes a base64 string to -> an image.
# def base64_to_image(base64_string):
#     # Decode the base64 string
#     byte_data = base64.b64decode(base64_string)
#     # Use BytesIO to convert the byte data to image
#     return Image.open(BytesIO(byte_data))


# # Creates an instance of Manager class from lida library and sets up a text generation configuration.
# lida = Manager(text_gen=llm("openai"))
# textgen_config = TextGenerationConfig(
#     n=1, temperature=0.5, model="gpt-3.5-turbo", use_cache=True
# )

# # Uses Streamlit to create a dropdown menu in the sidebar.
# menu = st.sidebar.selectbox("Choose an Option", ["Summarize", "Question based Graph"])


# import base64
# import streamlit as st
# from lida import Manager, TextGenerationConfig, llm
# from dotenv import load_dotenv
# import os
# import openai
# from PIL import Image
# from io import BytesIO
# import tempfile  # For handling temporary files

# # Load environment variables and set the OpenAI API key
# load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")


# # Define a function to decode a base64 string to an image
# def base64_to_image(base64_string):
#     byte_data = base64.b64decode(base64_string)
#     return Image.open(BytesIO(byte_data))


# # Create an instance of Manager class from lida library
# lida = Manager(text_gen=llm("openai"))
# textgen_config = TextGenerationConfig(
#     n=1, temperature=0.5, model="gpt-3.5-turbo", use_cache=True
# )

# # Streamlit UI setup
# menu = st.sidebar.selectbox("Choose an Option", ["Summarize", "Question based Graph"])


# # Handle file upload and processing
# def handle_file_processing(uploaded_file):
#     with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp_file:
#         tmp_file.write(uploaded_file.getvalue())
#         tmp_filename = tmp_file.name

#     # Process the file using lida library
#     summary = lida.summarize(
#         tmp_filename, summary_method="default", textgen_config=textgen_config
#     )
#     st.write(summary)

#     goals = lida.goals(summary, n=2, textgen_config=textgen_config)
#     for goal in goals:
#         st.write(goal)

#     charts = lida.visualize(
#         summary=summary, goal=goals[0], textgen_config=textgen_config, library="seaborn"
#     )
#     if charts:
#         img_base64_string = charts[0].raster
#         img = base64_to_image(img_base64_string)
#         st.image(img)
#     else:
#         st.write("No charts were generated.")
#     os.remove(tmp_filename)  # Ensure the temporary file is deleted after processing

# # choice 1
# if menu == "Summarize":

#     # Displays a subheader and a file uploader for uploading CSV files.
#     st.subheader("Summarization of your Data")
#     file_uploader = st.file_uploader("Upload your CSV", type="csv")

#     # If a file is uploaded, it saves it locally as "filename.csv".
#     if file_uploader is not None:
#         handle_file_processing(file_uploader)

#         # Summarizes the content of the CSV file using the lida library and displays the summary
#         summary = lida.summarize(
#             "filename.csv", summary_method="default", textgen_config=textgen_config
#         )
#         st.write(summary)

#         # Extracts goals from the summary and displays them.
#         goals = lida.goals(summary, n=2, textgen_config=textgen_config)
#         for goal in goals:
#             st.write(goal)

#         # Sets up configuration for visualization and generates charts based on the summary and the selected goal.
#         i = 0
#         library = "seaborn"
#         textgen_config = TextGenerationConfig(n=1, temperature=0.2, use_cache=True)
#         charts = lida.visualize(
#             summary=summary,
#             goal=goals[i],
#             textgen_config=textgen_config,
#             library=library,
#         )

#         # Converts the generated chart into an image and displays it.
#         if charts:
#             img_base64_string = charts[0].raster
#             img = base64_to_image(img_base64_string)
#             st.image(img)
#         else:
#             st.write("No charts were generated.")

# # choice 2
# elif menu == "Question based Graph":

#     # Displays a subheader and a file uploader for uploading CSV files (for the second option).
#     st.subheader("Query your Data to Generate Graph")
#     file_uploader = st.file_uploader("Upload your CSV", type="csv")

#     # If a file is uploaded, it saves it locally as "filename1.csv" (for the second option).
#     if file_uploader is not None:
#         handle_file_processing(file_uploader)

#         # Displays a text area for the user to input a query.
#         text_area = st.text_area("Query your Data to Generate Graph", height=200)

#         # Checks if the "Generate Graph" button is clicked.
#         if st.button("Generate Graph"):

#             # If there is a query provided, it summarizes the CSV file, performs the query-based visualization,
#             # converts the generated chart into an image, and displays it.
#             if len(text_area) > 0:
#                 st.info("Your Query: " + text_area)
#                 lida = Manager(text_gen=llm("openai"))
#                 textgen_config = TextGenerationConfig(
#                     n=1, temperature=0.2, use_cache=True
#                 )
#                 summary = lida.summarize(
#                     "filename1.csv",
#                     summary_method="default",
#                     textgen_config=textgen_config,
#                 )
#                 user_query = text_area
#                 charts = lida.visualize(
#                     summary=summary, goal=user_query, textgen_config=textgen_config
#                 )
#                 charts[0]
#                 image_base64 = charts[0].raster
#                 img = base64_to_image(image_base64)
#                 st.image(img)


import base64
import streamlit as st
from lida import Manager, TextGenerationConfig, llm
from dotenv import load_dotenv
import os
import openai
from PIL import Image
from io import BytesIO
import tempfile  # For handling temporary files

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


# Function to handle file upload and processing
def handle_file_processing(uploaded_file, file_name):
    path_to_save = os.path.join(
        tempfile.gettempdir(), file_name
    )  # Save file in temp directory
    with open(path_to_save, "wb") as f:
        f.write(uploaded_file.getvalue())

    return path_to_save


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
    summary = lida.summarize(file_path, summary_method="default", textgen_config=textgen_config)
    st.write(summary)

    charts = lida.visualize(summary=summary, goal=query, textgen_config=textgen_config)
    if charts:
        img_base64_string = charts[0].raster
        img = base64_to_image(img_base64_string)
        st.image(img)
    else:
        st.write("No charts generated.")


if menu == "Summarize":
    st.subheader("Summarization of your Data")
    file_uploader = st.file_uploader("Upload your CSV", type="csv")
    if file_uploader is not None:
        file_path = handle_file_processing(file_uploader, "summarize_filename.csv")
        summarize_data(file_path)

# Choice for 'Question based Graph'
if menu == "Question based Graph":
    st.subheader("Query your Data to Generate Graph")
    file_uploader = st.file_uploader("Upload your CSV", type="csv")
    text_area = st.text_area("Enter your query here:", height=200)
    if st.button("Generate Graph") and file_uploader and text_area:
        file_path = handle_file_processing(file_uploader, "query_filename.csv")
        generate_query_based_graph(file_path, text_area)
        os.remove(file_path)
