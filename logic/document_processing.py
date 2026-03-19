from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from typing import List
from dotenv import load_dotenv

load_dotenv()

# Step 1: Document Loader
def loading_document(file_path: str) -> List[Document]:
    loader = PyPDFLoader(file_path=file_path)
    return loader.load()

# Step 2: Text Splitting
def spliting_texts(docs: List[Document]) -> List[Document]:
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        add_start_index = True
    )

    return text_splitter.split_documents(docs)

# Step 3: Storing into Database
def storing_vector_db(splited_texts: List[Document]) -> Chroma:
    embedding = OpenAIEmbeddings(model="text-embedding-3-large")
    vector_db = Chroma.from_documents(
        documents= splited_texts,
        embedding= embedding,
        collection_name = "ai_agent_tutorial",
        persist_directory= "./logic/vector_db_rag_tutorial"
    )

    return vector_db

# Step 4: Initialization function 
def process_document_for_rag(file_path: str) -> None:
    while True:
        try:
            print("Loading the document")
            docs_loaded = loading_document(file_path=file_path)
        except Exception as e:
            print("Oops...file loading faceing an error..\n", e)
            break

        try:
            print("Chunking started...")
            splitted_chunks = spliting_texts(docs=docs_loaded)
        except Exception as e:
            print("Oh no! Chunking failed...\n", e)
            break

        try:
            print("Storing into vector database for query...")
            storing_vector_db(splited_texts=splitted_chunks)
        except Exception as e:
            print("Sorry, can't save into Vector DB...\n", e)
            break
        finally:
            print("Initialization completed!\nCONGRATULATIONS")
            break
        
    return None
