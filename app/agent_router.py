# app/agent_router.py

from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

from app.vector_store import load_vector_store
from app.retriever import get_retriever
from app.llm import load_llm
from app.intent_classifier import classify_intent
from app.prompts import get_prompt
from app.user_memory import UserMemory
from app.recommender import get_personalized_context
from app.genre_extractor import extract_genre
from app.auth import AuthManager


class EntertainmentAgent:

    def __init__(self):
        self.vector_db = load_vector_store()
        self.retriever = get_retriever(self.vector_db)
        self.llm = load_llm()
        self.memory = UserMemory()
        self.auth = AuthManager()
        self.current_user = None

    def login(self, username):
        self.auth.register(username)
        self.memory.init_user(username)
        self.current_user = username

    def handle_query(self, query: str):

        if not self.current_user:
            return {"intent": "auth", "response": "Please login first."}

        if query.lower().startswith("rate"):
            parts = query.split()
            rating = float(parts[-1])
            title = " ".join(parts[1:-1])
            self.memory.add_rating(self.current_user, title, rating)
            return {"intent": "rating", "response": "Rating saved."}

        intent = classify_intent(query)
        prompt_template = get_prompt(intent)
        prompt = ChatPromptTemplate.from_template(prompt_template)

        user_data = self.memory.get_user(self.current_user)

        if intent == "recommendation":
            documents, explanation = get_personalized_context(
                self.retriever,
                query,
                user_data
            )
        else:
            documents = self.retriever.invoke(query)
            explanation = ""

        chain = create_stuff_documents_chain(self.llm, prompt)

        response = chain.invoke({
            "input": query,
            "context": documents
        })

        if intent == "recommendation" and documents:
            top_doc = documents[0]
            title = top_doc.metadata.get("title")
            genre = extract_genre(top_doc)

            self.memory.add_history(self.current_user, title)
            self.memory.add_genre_preference(self.current_user, genre)

            response += f"\n\nRecommendation Score Details:\n{explanation}"

        return {
            "intent": intent,
            "response": response.strip()
        }
