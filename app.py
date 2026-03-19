import streamlit as st

from treerag.parser import extract_text_from_pdf
from treerag.tree_builder import build_tree
from treerag.navigator import navigate_tree
from treerag.answerer import generate_answer
from treerag.scorer import compute_confidence


st.set_page_config(page_title="TreeRAG 🌳", layout="wide")

st.title("🌳 TreeRAG — Document Navigator")

# Load document (run once)
@st.cache_resource
def load_document():
    pdf_path = "data/sample.pdf"
    pages = extract_text_from_pdf(pdf_path)
    root = build_tree(pages)
    return root


root = load_document()

# Input box
question = st.text_input("Ask a question about the document:")

if question:
    final_nodes, paths = navigate_tree(question, root)
    answer = generate_answer(question, final_nodes)
    confidence = compute_confidence(question, final_nodes, paths)

    st.subheader("📌 Answer")
    st.write(answer)

    st.subheader("🧠 Reasoning Paths")
    for path in paths:
        st.write(" → ".join(path))

    st.subheader("📊 Confidence")
    st.write(f"{confidence}%")