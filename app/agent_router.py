# app/agent_router.py

from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain

from app.vector_store import load_vector_store
from app.retriever import get_retriever
from app.llm import load_llm
from app.intent_classifier import classify_intent
from app.prompts import get_prompt


class EntertainmentAgent:

    def __init__(self):
        self.vector_db = load_vector_store()
        self.retriever = get_retriever(self.vector_db)
        self.llm = load_llm()

    def handle_query(self, query: str):

        intent = classify_intent(query)
        prompt_template = get_prompt(intent)

        prompt = ChatPromptTemplate.from_template(prompt_template)

        document_chain = create_stuff_documents_chain(
            self.llm,
            prompt
        )

        retrieval_chain = create_retrieval_chain(
            self.retriever,
            document_chain
        )

        response = retrieval_chain.invoke({
            "input": query
        })

        return {
            "intent": intent,
            "response": response["answer"].strip()
        }
