import streamlit as st
from api_client import ask_question

st.set_page_config(
    page_title="Diabetes RAG Assistant",
    page_icon="🩺",
    layout="centered",
)

st.title("🩺 Diabetes RAG Assistant")
st.caption(
    "Ask questions about diabetes and get answers "
    "based on the provided knowledge base."
)

st.markdown("---")

question = st.text_area(
    "Ask your question",
    placeholder="e.g. What are the risk factors for type 2 diabetes?",
    height=100,
)

if st.button("Ask", type="primary", use_container_width=True):
    if not question.strip():
        st.warning("Please enter a question first.")

    else:
        with st.spinner("Searching the knowledge base and generating an answer..."):
            try:
                result = ask_question(question.strip())

                st.subheader("Answer")
                st.write(result.get("answer", "No answer returned."))

                sources = result.get("sources", [])

                if sources:
                    st.subheader("Sources")

                    for i, source in enumerate(sources, start=1):
                        title = source.get(
                            "source",
                            f"Source {i}"
                        )

                        page = source.get("page", "N/A")
                        section_id = source.get("section_id", "N/A")
                        text = source.get("text", "")

                        with st.expander(
                            f"{title} | Page {page}"
                        ):
                            st.write(f"**Section:** {section_id}")
                            st.write(text)

            except Exception as e:
                st.error(
                    "Could not connect to the backend. "
                    "Make sure the FastAPI server is running."
                )
                st.caption(str(e))