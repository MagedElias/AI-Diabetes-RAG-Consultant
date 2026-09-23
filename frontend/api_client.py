
import requests


BACKEND_URL = "http://127.0.0.1:8000"


def ask_question(question: str) -> dict:
    """
    Send a question to the local FastAPI backend
    and return the answer with its sources.
    """

    response = requests.post(
        f"{BACKEND_URL}/query",
        json={"question": question},
        timeout=180,
    )

    response.raise_for_status()

    return response.json()