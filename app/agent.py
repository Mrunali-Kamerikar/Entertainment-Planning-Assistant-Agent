import os
from dotenv import load_dotenv

from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

from langchain_core.prompts import ChatPromptTemplate

# FIXED IMPORTS
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_classic.chains.retrieval import create_retrieval_chain

# Load API key
load_dotenv()

def create_agent():
    try:
        print("Loading embedding model...")

        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        print("Loading vector database...")

        vector_db = Chroma(
            persist_directory="data/vector_db",
            embedding_function=embedding_model
        )

        retriever = vector_db.as_retriever(
            search_type="mmr",   # Maximum Marginal Relevance (diverse results)
            search_kwargs={"k": 5, "fetch_k": 10}
        )


        print("Connecting to LLM...")

        print("Loading free HuggingFace LLM...")

        pipe = pipeline(
            "text2text-generation",
            model="google/flan-t5-base",
            max_new_tokens=256,
            do_sample=True,        # enable randomness
            temperature=0.7,       # control creativity
            top_p=0.9
        )

        llm = HuggingFacePipeline(pipeline=pipe)

        print("Creating prompt...")

        prompt = ChatPromptTemplate.from_template(
            """
            You are an entertainment recommendation assistant.

            Based on the context below, recommend ONE movie and explain briefly why.

            Context:
            {context}

            Question:
            {input}

            Recommendation:
            """
        )

        print("Creating document chain...")

        document_chain = create_stuff_documents_chain(llm, prompt)

        print("Creating retrieval chain...")

        retrieval_chain = create_retrieval_chain(retriever, document_chain)

        print("Agent ready.")

        return retrieval_chain

    except Exception as e:
        print("Error creating agent:", e)
        return None


def ask_agent(question):

    agent = create_agent()

    if agent is None:
        return

    print("\nQuestion:", question)

    response = agent.invoke({
        "input": question
    })

    print("\nAnswer:")
    print(response["answer"])


if __name__ == "__main__":

    ask_agent(input("Enter your question: "))
