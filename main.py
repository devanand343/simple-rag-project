import os
from logic import document_processing, agent

document_path = "./logic/codewave-com-insights-build-ai-agents-beginners-guide-.pdf"
vector_db_path = "./logic/vector_db_rag_tutorial"

if not os.path.exists(vector_db_path):

    print("Running initialization...")
    try:
        document_processing.process_document_for_rag(file_path=document_path)
    except Exception as e:
        print("Initialization of doument is failed. ", e)
        exit()

while True:
    user_query = input("What's on your mind today?\n>>> ")
    if user_query.lower() == "exit":
        break
    print(agent.ask_agent(user_query))




