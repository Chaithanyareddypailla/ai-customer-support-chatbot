from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import CharacterTextSplitter


def load_knowledge():
    with open("data/faq.txt", "r") as f:
        text = f.read()

    splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=20)
    docs = splitter.split_text(text)

    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma.from_texts(docs, embeddings)

    return db
