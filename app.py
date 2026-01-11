from search import retrieve_documents
from rag import generate_answer

def main():
    username = "Karthik"   # folder name in blob
    question = "What is casual leave?"

    print("🔍 Searching documents...")
    docs = retrieve_documents(username, question)

    print("🤖 Generating answer...")
    answer = generate_answer(question, docs)

    print("\n" + "="*60)
    print("QUESTION:", question)
    print("-"*60)
    print("ANSWER:")
    print(answer)
    print("="*60)

if __name__ == "__main__":
    main()
