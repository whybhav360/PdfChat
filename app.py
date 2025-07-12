import streamlit as st
import fitz  
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline

def get_pdf_text(pdf_docs, max_pages=10):
    text = ""
    for pdf in pdf_docs:
        doc = fitz.open(stream=pdf.read(), filetype="pdf")
        for i, page in enumerate(doc):
            if i >= max_pages:
                break
            text += page.get_text()
    return text

def get_text_chunks(text):
    splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200)
    return splitter.split_text(text)

def get_vectorstore(chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.from_texts(texts=chunks, embedding=embeddings)

def get_qa_chain(vectorstore):
    flan = pipeline(
        "text2text-generation",
        model="google/flan-t5-small",
        tokenizer="google/flan-t5-small",
        max_length=150,
        temperature=0.0,
    )
    llm = HuggingFacePipeline(pipeline=flan)
    return RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())

def main():
    st.set_page_config(page_title="Document Searcher", page_icon="📄")
    st.title("Ask Questions About Your PDFs")

    pdf_docs = st.file_uploader("Upload one or more PDFs", type="pdf", accept_multiple_files=True)
    if pdf_docs:
        with st.spinner("processing PDF(s)"):
            raw_text = get_pdf_text(pdf_docs)
            if not raw_text.strip():
                st.error("No text found in the uploaded PDFs.")
                return

            chunks = get_text_chunks(raw_text)
            vectorstore = get_vectorstore(chunks)
            qa_chain = get_qa_chain(vectorstore)
            st.success("Ask a question below:")

            question = st.text_input("Ask a question:")
            if question:
                with st.spinner("Generating answer..."):
                    custom_prompt = f"Answer concisely in 5-6 sentences: {question}"
                    result = qa_chain.run(custom_prompt)
                    st.write("### 🤖 Answer:")
                    st.write(result)

if __name__ == "__main__":
    main()
