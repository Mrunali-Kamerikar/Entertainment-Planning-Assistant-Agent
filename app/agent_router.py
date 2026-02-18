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


class EntertainmentAgent:

    def __init__(self):
        self.vector_db = load_vector_store()
        self.retriever = get_retriever(self.vector_db)
        self.llm = load_llm()
        self.memory = UserMemory()

    def handle_query(self, query: str):

        # Handle rating command
        if query.lower().startswith("rate"):
            parts = query.split(" ", 2)
            if len(parts) == 3:
                _, title, rating = parts
                self.memory.add_rating(title, float(rating))
                return {
                    "intent": "rating",
                    "response": f"Rating saved for {title}"
                }

        intent = classify_intent(query)
        prompt_template = get_prompt(intent)

        prompt = ChatPromptTemplate.from_template(prompt_template)

        user_memory = self.memory.get_memory()

        if intent == "recommendation":
            documents = get_personalized_context(
                self.retriever,
                query,
                user_memory
            )
        else:
            documents = self.retriever.get_relevant_documents(query)

        context_text = "\n\n".join([doc.page_content for doc in documents])

        chain = create_stuff_documents_chain(
            self.llm,
            prompt
        )

        response = chain.invoke({
            "context": context_text,
            "input": query
        })

        # Store recommendation history
        if intent == "recommendation":
            if documents:
                title = documents[0].metadata.get("title")
                self.memory.add_history(title)

        return {
            "intent": intent,
            "response": response.strip()
        }
