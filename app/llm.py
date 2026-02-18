# app/llm.py

from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from app.config import LLM_MODEL, MAX_OUTPUT_TOKENS


def load_llm():

    pipe = pipeline(
        "text2text-generation",
        model=LLM_MODEL,
        max_new_tokens=MAX_OUTPUT_TOKENS,
        do_sample=True,
        temperature=0.7,
        top_p=0.9
    )

    return HuggingFacePipeline(pipeline=pipe)

