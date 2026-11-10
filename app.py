import streamlit as st

st.set_page_config(
    page_title="WAFAA-AI",
    page_icon="👶",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #F8F5FC;
}
h1, h2, h3 {
    color: #68458A;
}
.stButton button {
    background-color: #7952A3;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("WAFAA-AI")
st.subheader("Because Every Cry Has a Meaning")

st.write("""
An experimental AI-powered infant cry analysis platform.
""")

st.divider()

st.header("Cry Analysis")

audio = st.file_uploader(
    "Upload an infant cry recording",
    type=["wav", "mp3", "ogg"]
)

if audio is not None:
    st.audio(audio)
    st.info("Audio uploaded successfully. Model integration is the next step.")

st.divider()

st.header("Acoustic Profile")
st.write("Acoustic measurements will appear here.")

st.header("Baby Profiles")
st.write("Baby profile management will appear here.")

st.header("Lullabies")
st.write("Lullabies and gentle ambient sounds will appear here.")

st.caption("WAFAA-AI Research Prototype | Not a medical diagnostic tool")
