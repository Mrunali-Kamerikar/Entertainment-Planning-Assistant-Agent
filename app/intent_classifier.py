# app/intent_classifier.py

def classify_intent(query: str) -> str:
    q = query.lower()

    if any(word in q for word in ["recommend", "suggest"]):
        return "recommendation"
    elif any(word in q for word in ["summary", "summarize"]):
        return "summary"
    elif "review" in q:
        return "review"
    elif any(word in q for word in ["why", "reflect", "analysis"]):
        return "reflection"
    else:
        return "qna"
