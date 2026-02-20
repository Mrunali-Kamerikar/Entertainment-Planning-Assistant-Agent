# 🎬 Agentic AI – Entertainment Planning Assistant

A production-ready **Agentic AI-powered Entertainment Recommendation Platform** built using:

* 🐍 Python
* 🧠 LangChain
* 🤗 HuggingFace LLM
* 🗂 Chroma Vector Database
* 🎨 Streamlit (Frontend)

This project simulates a **Netflix-style intelligent entertainment assistant** with:

* Personalized movie recommendations
* Multi-user login system
* Rating-based ranking
* Genre preference learning
* Explainable AI scoring
* Summary, Review, Q&A generation



# 🚀 Features

## 🔐 Multi-User System

* Separate user profiles
* Persistent memory per user
* Personalized recommendation logic

## 🎯 Intelligent Recommendation Engine

* Semantic similarity search
* Weighted ranking algorithm
* Rating boost
* Genre preference boost
* History penalty (avoid repetition)

## ⭐ User Rating System

Users can rate movies:

```
rate <movie_name> <rating>
```

Ratings influence future recommendations.

## 🎭 Genre Learning

System automatically:

* Extracts genre from metadata
* Learns user preference trends
* Boosts preferred genres in ranking

## 🧠 Explainable AI

Each recommendation includes:

* Final score
* Similarity score
* Rating boost
* Genre boost
* History penalty

Transparent decision-making process.

## 📚 Content Generation Modes

Supports:

* Recommendation
* Summary
* Review
* Reflection
* Q&A



# 🏗️ Architecture

```
Frontend (Streamlit)
        ↓
Agent Router
        ↓
Intent Classification
        ↓
Vector Search (Chroma)
        ↓
Similarity Scoring
        ↓
Ranking Engine
        ↓
LLM Generation
```



# 📂 Project Structure

```
Agentic_AI_Project/
│
├── app/
│   ├── agent_router.py
│   ├── auth.py
│   ├── config.py
│   ├── embeddings.py
│   ├── genre_extractor.py
│   ├── intent_classifier.py
│   ├── llm.py
│   ├── ranking.py
│   ├── recommender.py
│   ├── user_memory.py
│   ├── vector_store.py
│   └── main.py
│
├── frontend/
│   └── streamlit_app.py
│
├── data/
│   ├── user_memory.json
│   └── vector_db/
│
└── README.md
```



# 🧠 Ranking Formula

Final recommendation score is computed as:

```
Final Score =
    (1 - similarity_distance)
    + (rating × 0.5)
    + (genre_preference × 0.3)
    - history_penalty
```

Where:

* Similarity is semantic match
* Ratings boost preferred movies
* Genre preference increases over time
* History prevents repetition



# ⚙️ Installation

## 1️⃣ Create Virtual Environment

```bash
python -m venv entertainment_agent
```

Activate:

Windows:

```bash
entertainment_agent\Scripts\activate
```

Mac/Linux:

```bash
source entertainment_agent/bin/activate
```



## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If no requirements file, install manually:

```bash
pip install langchain langchain-chroma langchain-huggingface
pip install chromadb
pip install sentence-transformers
pip install transformers torch
pip install streamlit
```



# ▶️ Running the Backend (CLI Mode)

```bash
python -m app.main
```

You will be prompted:

```
Enter username to login:
```



# 🎨 Running the Frontend (Streamlit UI)

```bash
streamlit run frontend/streamlit_app.py
```

Open browser at:

```
http://localhost:8501
```



# 🧪 Example Usage

### Recommend

```
recommend a sad movie
```

### Summarize

```
summarize Grave of the Fireflies
```

### Review

```
give review of When Marnie Was There
```

### Rate

```
rate Grave of the Fireflies 5
```



# 💾 Persistent Memory

User preferences are stored in:

```
data/user_memory.json
```

Supports:

* Ratings
* Genre preferences
* Recommendation history



# 🛠 Tech Stack

| Layer             | Technology             |
| ----------------- | ---------------------- |
| LLM               | Google FLAN-T5         |
| Embeddings        | Sentence Transformers  |
| Vector DB         | Chroma                 |
| Backend Framework | LangChain              |
| Frontend          | Streamlit              |
| Storage           | JSON-based persistence |



# 🧩 Future Enhancements

* Collaborative filtering
* Poster image integration
* Real movie API (TMDB integration)
* FastAPI production backend
* Docker deployment
* Cloud deployment (Render / AWS / GCP)



# 📌 Learning Outcomes

This project demonstrates:

* Agentic AI system design
* Retrieval-Augmented Generation (RAG)
* Personalization algorithms
* Explainable AI scoring
* Multi-user architecture
* Production-ready modular backend
* Fullstack AI application development



# 👩‍💻 Author

**Mrunali Kamerikar**
B.Tech – 8th Semester
Agentic AI Project



# 📄 License

This project is for educational and research purposes.

