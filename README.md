# 🚀 DataWhisperer: AI-Powered Data Intelligence

**DataWhisperer** is an advanced Agentic AI platform that bridges the gap between natural language and complex relational databases. Built for the **Antigravity ecosystem**, it allows users to **chat with their data in real-time**, leveraging high-performance LLMs to automate SQL generation and data synthesis.

---

# 🧠 The "Agentic" Core

Unlike simple chatbots, **DataWhisperer uses an Agentic Loop**.  
When a user asks a question, the AI (**Llama 3.3 70B**) doesn't just guess an answer. It:

1. **Reasons** about the intent of the question  
2. **Decides** which internal API tool is required  
3. **Executes** a live database call  
4. **Synthesizes** the raw JSON results into a natural, human-readable insight  

---

# 🛠️ Tech Stack

## Backend

- **FastAPI** — High-performance Python framework for the core API
- **Groq SDK** — Lightning-fast inference using Llama 3.3 70B
- **SQLAlchemy** — Robust ORM for PostgreSQL / Neon database management
- **Pydantic** — Strict data validation and settings management

## Frontend

- **Next.js 14** — React framework for a seamless server-side rendered dashboard
- **Tailwind CSS** — Professional "Antigravity" dark-mode styling
- **Lucide React** — Clean, consistent iconography

---

# 🚀 Key Features

### Natural Language Querying
Ask questions like:

> *"Which city has the highest 1-star reviews?"*

and get instant answers.

### Real-Time Monitoring
Track success rates and processing times through a sleek visual dashboard.

### Tool-Calling Architecture
Extensible system for adding new data transformation and retrieval tools.

### Secure Infrastructure
Environment-based configuration for API keys and database credentials.

---

# ⚙️ Getting Started

## 1. Prerequisites

- Python **3.12+** (Optimized for Python 3.14 compatibility)
- Node.js **18+**
- A **Groq API Key**

---

# Backend Setup

```bash
cd backend

python -m venv venv

# Activate environment
source venv/bin/activate
# Windows:
# .\venv\Scripts\activate

pip install -r requirements.txt

# Create a .env file containing:
# GROQ_API_KEY=your_key
# DATABASE_URL=your_database_url

uvicorn app.main:app --reload
```

---

# Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

# 📊 Roadmap

- [x] Core Agentic Loop & Tool Calling  
- [x] FastAPI & Next.js Integration  
- [ ] NextAuth.js User Authentication  
- [ ] Real-time Data Visualization (Recharts)  
- [ ] Multi-tenant Team Management  

---

# 🤝 Contributors

**Ismail Khamal Arbit**  

**Taymas Ihssan**  
