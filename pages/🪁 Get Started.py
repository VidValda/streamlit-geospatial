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


def app():
    st.title("Search engine")
    st.markdown(
        """
    Insert your prompt, we suggest to use [Lexica](https://lexica.art/) for better results.   
    """
    )

    with st.expander("See demo"):
        st.image("https://i.imgur.com/0SkUhZh.gif")

    row1_col1, row1_col2 = st.columns([3, 1])
    width = 800
    height = 600
    tiles = None

    with row1_col2:

        checkbox = st.text("Insert prompt")
        keyword = st.text_input("Enter an image idea:")
        empty = st.empty()

        if keyword:
            print(keyword)
        with row1_col1:
            st.image("https://64.media.tumblr.com/8817258bf5f20787e292180c2cffff6e/3ffb98050a7580c4-63/s540x810/713a25af57ff905b845e44d50f186271064aadeb.gifv")




app()
