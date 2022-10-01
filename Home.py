import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

st.sidebar.title("Contact")
st.sidebar.info(
    """
    Qiusheng Wu: <https://wetlands.io>
    [GitHub](https://github.com/giswqs) | [Twitter](https://twitter.com/giswqs) | [YouTube](https://www.youtube.com/c/QiushengWu) | [LinkedIn](https://www.linkedin.com/in/qiushengwu)
    """
)



st.title("Text to Image with NASA Biased Dataset")

st.markdown(
    """
    In this web you can give a text input and have an image output, this is made via [Stable Diffusion](https://github.com/CompVis/stable-diffusion) with some modifications so the NASA dataset can be merged.

    """
)

st.info("Enter to the get Started Page.")

st.subheader("Examples of Images and their prompts")
st.markdown(
    """
    The following images where genereted via the merged models of Stable Diffusion and NASA Dataset.
    """
)

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.image("https://64.media.tumblr.com/8817258bf5f20787e292180c2cffff6e/3ffb98050a7580c4-63/s540x810/713a25af57ff905b845e44d50f186271064aadeb.gifv")
    st.image("https://preview.redd.it/hiii-everyone-i-made-a-local-deforum-stable-diffusion-ver-v0-xn1e7x9k9mn91.gif?width=480&auto=webp&s=38e34a2bb39c14a68304c18fb699d5e0817072a4")

with row1_col2:
    st.image("https://cdnb.artstation.com/p/assets/images/images/050/680/403/original/seedmole-seedmoleanimtest3.gif?1655410947")
    st.image("https://c.tenor.com/0HG-oUyC45EAAAAC/magic-man-ai-art.gif")
