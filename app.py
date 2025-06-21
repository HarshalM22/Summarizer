import streamlit as st
from src.utils import write_file
from src.text_cleaner import clean_text
from src.summarizer import summarize
from src.keyword_extractor import extract_keywords
from src.config import SUMMARY_SENTENCES, KEYWORD_COUNT

st.set_page_config(page_title="Text Summarizer & Keyword Extractor", layout="centered")
st.title("🧠 Text Summarizer & 🔑 Keyword Extractor")

st.markdown("You can either **paste your text** or **upload a `.txt` file**.")

# Input Option 1: Text Box
text_input = st.text_area("✍️ Paste your text here", height=200)

# Input Option 2: File Upload
uploaded_file = st.file_uploader("📂 Or upload a .txt file", type=["txt"])

raw_text = ""
if text_input:
    raw_text = text_input
elif uploaded_file:
    raw_text = uploaded_file.read().decode("utf-8")

if raw_text:
    st.subheader("📄 Preview of Input Text")
    st.write(raw_text[:500] + "..." if len(raw_text) > 500 else raw_text)

    if st.button("🚀 Generate Summary and Keywords"):
        cleaned = clean_text(raw_text)
        summary = summarize(cleaned, SUMMARY_SENTENCES)
        keywords = extract_keywords(cleaned, KEYWORD_COUNT)

        write_file("outputs/summary.txt", summary)
        write_file("outputs/keywords.txt", "\n".join(keywords))

        st.subheader("📝 Summary")
        st.success(summary)

        st.subheader("🔑 Keywords")
        st.write(", ".join(keywords))

        with st.expander("📁 Download Results"):
            st.download_button("📥 Download Summary", summary, file_name="summary.txt")
            st.download_button("📥 Download Keywords", "\n".join(keywords), file_name="keywords.txt")
else:
    st.info("Paste text above or upload a file to get started.")
