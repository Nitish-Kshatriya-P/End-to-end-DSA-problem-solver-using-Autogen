# DSA Wizard 🧙‍♂️ – Multi-Agent AI DSA Problem Solver

## 📌 Overview

    AlgoGenie is a multi-agent AI system that autonomously solves Data Structures & Algorithms (DSA) problems.
    It orchestrates a Problem Fetcher Agent, Problem Solver Agent, and Code Executor Agent to:
    
    1. Fetch problems directly from a given URL.
    2. Generate clean, optimized Python solutions.
    3. Iteratively debug and validate against test cases.
    4. Deliver a final, production-ready solution.
    
    This project demonstrates agentic AI, LLM-powered workflows, and containerized execution for practical problem-solving.

## ⚙️ Features

    🔗 URL-based Problem Fetching – Automatically scrapes DSA problems with constraints & test cases.
  
    🧠 Autonomous Problem Solving – LLM-based agent generates structured solution plans and Python code.
  
    ✅ Iterative Debugging & Validation – Code Executor Agent tests and refines until all cases pass.
  
    📂 Solution Export – Saves the final verified solution as solution.py.
  
    🖥️ Interactive UI – Built with Streamlit for seamless user experience.
  
    🐳 Docker Integration – Sandboxed code execution for security and reproducibility.

## 🏗️ Architecture

             User Input (DSA Problem URL)
                        ↓
     Problem Fetcher Agent (Web Scraper + Parser)
                        ↓
    Problem Solver Agent (LLM-powered Solution Generator)
                        ↓
     Code Executor Agent (Runs & Validates Code in Docker)
                        ↓
       Final Solution (solution.py + Explanation)

## 🚀 Getting Started

    1️⃣ Clone the Repository
    git clone https://github.com/your-username/algo-genie.git
    cd algo-genie
    
    2️⃣ Install Dependencies
    pip install -r requirements.txt
    
    3️⃣ Run the App
    streamlit run app.py
    or
    streamlit run app.py

## 🧑‍💻 Tech Stack

    Python 3.9+
    
    Streamlit – Interactive UI
    
    Autogen / LLMs (OpenAI) – Multi-agent orchestration
    
    Docker – Secure sandbox for code execution
    
    Crawl4AI – Web scraping for problem statements

## 📊 Example Workflow

    Paste a DSA problem URL (e.g., LeetCode, GeeksforGeeks).
    
    Agents collaborate to fetch, solve, and test the problem.
    
    Download the verified Python solution (solution.py).
