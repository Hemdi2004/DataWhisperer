# 🚀 DataWhisperer: AI-Powered Data Intelligence

**DataWhisperer** is an advanced Agentic AI platform that bridges the gap between natural language and complex relational databases. Built for the **Antigravity ecosystem**, it allows users to **chat with their data in real-time**, leveraging high-performance LLMs to automate SQL generation and data synthesis.

---

# 🧠 The "Agentic" Core

Unlike simple chatbots, **DataWhisperer uses an Agentic Loop**.  
When a user asks a question, the AI (**Llama 3.3 70B**) doesn't just guess an answer. It:

1. **Reasons** about the intent of the question by mapping it to a dynamically discovered database schema.
2. **Generates** and safely executes raw read-only SQL queries natively against your data.
3. **Retrieves** a live database result.
4. **Synthesizes** the raw JSON results into a natural, human-readable insight. 

---

# 🛠️ Tech Stack

## Backend

- **FastAPI** — High-performance Python framework for the synchronously secure core API.
- **Groq SDK** — Lightning-fast inference using Llama 3.3 70B.
- **SQLAlchemy** — Robust ORM for PostgreSQL / Neon database management and universal schema discovery.
- **Pydantic & Jose JWT** — Strict data validation and fully integrated OAuth2 access token security.

## Frontend

- **Next.js 14** — React framework for a seamless server-side rendered dashboard.
- **Tailwind CSS** — Professional "Antigravity" dark-mode styling.
- **NextAuth.js** — Robust and fully-managed user authentication integrated with the FastAPI backend.
- **Lucide React** — Clean, consistent iconography.

---

# 🚀 Key Features

### Natural Language Querying
Ask questions like:

> *"Which city has the highest 1-star reviews?"*

and get instant answers powered by dynamic, live-generated SQL.

### Secure & Read-Only AI Interactions
The agent respects a synchronized sandbox, guaranteeing that all generated SQL code is strictly verified as `SELECT` operations only, preventing destructive queries.

### Real-Time Monitoring
Track success rates and processing times through a sleek visual dashboard.

### Secure Infrastructure
Environment-based configuration for API keys, secure secret management, and robust JWT session validation.

---

# ⚙️ Getting Started

## 1. Prerequisites

- Python **3.12+** (Optimized for Python 3.14 compatibility)
- Node.js **18+**
- A **Groq API Key**
- A deployed conversational **PostgreSQL** database (e.g., Neon)

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
# JWT_SECRET_KEY=your_secure_secret_hash

uvicorn app.main:app --reload
```

---

# Frontend Setup

```bash
cd frontend

npm install

# Create a .env.local file containing your FastAPI URL and NextAuth secret
# NEXT_PUBLIC_API_URL=http://localhost:8000
# NEXTAUTH_SECRET=your_nextauth_secret_hash
# NEXTAUTH_URL=http://localhost:3000

npm run dev
```

---

# 📊 Roadmap

- [x] Core Agentic Loop & Dynamic SQL Tool Calling  
- [x] FastAPI & Next.js Integration  
- [x] JWT Backend & NextAuth.js User Authentication  
- [ ] Real-time Data Visualization (Recharts)  
- [ ] Multi-tenant Team Management  

---

# 🤝 Contributors

**Ismail Khamal Arbit**  

**Taymas Ihssan**  
