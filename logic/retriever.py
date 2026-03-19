from langchain.tools import tool
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

@tool(response_format="content")
def retrieve_content_locally(query: str):
    """takes user query as string and search it into local vector database"""
    vector_store = Chroma(
        collection_name="ai_agent_tutorial",
        embedding_function= OpenAIEmbeddings(model="text-embedding-3-large"),
        persist_directory= "./logic/vector_db_rag_tutorial"
    )
    retrieve_docs = vector_store.similarity_search(
        query=query,
        k = 2
    )

    content = "\n\n".join(
        f"Content: {doc.page_content}"
        for doc in retrieve_docs
    )

    return  content