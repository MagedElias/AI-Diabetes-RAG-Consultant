from typing import List, Dict, Any


class GenerationService:
    """
    Responsible for generating an answer
    using the retrieved document context.
    """

    def __init__(self, llm=None):
        self.llm = llm

    def generate(
        self,
        question: str,
        contexts: List[Dict[str, Any]],
    ) -> str:
        """
        Generate an answer based on the question
        and retrieved contexts.
        """

        if not question.strip():
            return "Please provide a valid question."

        if not contexts:
            return "No relevant information was found."

        # Placeholder for the actual LLM generation logic.
        # The current RAG pipeline handles generation separately.
        return ""