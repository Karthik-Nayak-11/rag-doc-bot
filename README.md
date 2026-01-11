# Azure RAG Document Q&A Bot

This project implements a **Retrieval-Augmented Generation (RAG)** system that answers user questions based on internal PDF documents using the **Azure AI stack**.

The system retrieves relevant document content from Azure AI Search and generates grounded answers using Azure OpenAI.

---

## Architecture Overview

PDF Documents → Azure Blob Storage  
→ Azure AI Search (Index + Indexer)  
→ Azure OpenAI (GPT)  
→ Answer to User

---

## Key Features

- Server-side document filtering using blob folder paths
- Multi-user document isolation with a single shared index
- Secure configuration using environment variables
- Python-based retrieval and response generation
- Designed for internal policy and document Q&A use cases

---

## Project Structure
```
rag-doc-bot/
├── app.py # Main application entry point
├── search.py # Azure AI Search retrieval logic
├── rag.py # Azure OpenAI answer generation
├── config.py # Environment configuration loader
├── requirements.txt # Python dependencies
├── .env # Environment variables (not committed)
└── README.md
```


---

## Azure Services Used

- Azure Blob Storage (PDF storage)
- Azure AI Search (document indexing and retrieval)
- Azure OpenAI (LLM-based answer generation)

---

## How It Works

1. PDF files are uploaded to Azure Blob Storage under user-specific folders.
2. Azure AI Search indexes and chunks the documents.
3. Python code queries Azure AI Search with server-side filtering to retrieve relevant chunks.
4. Retrieved content is passed to Azure OpenAI to generate an answer grounded in the documents.

---

## Configuration

All credentials and endpoints are stored in a `.env` file:

- Azure AI Search endpoint, index name, and API key
- Azure OpenAI endpoint, deployment name, and API key
- Azure Blob Storage account URL and container name

---

## Limitations

- The current setup uses lexical search only.
- For large documents, front-matter sections may dominate retrieval results.
- Semantic or vector search would improve relevance for long documents.

---

## Future Improvements

- Enable semantic or vector-based search
- Improve chunking strategies
- Add answer citations and confidence scores
- Expose the system as a REST API

---

## Author

Karthik Nayak
