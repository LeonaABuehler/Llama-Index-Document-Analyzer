import os
from llama_index.llms.openai import OpenAI
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.memory import ChatMemoryBuffer

# Set API key
os.environ["OPENAI_API_KEY"] = "YOUR_API_KEY"

# Choose model
llm = OpenAI(model="gpt-4o")

# Load and index PDF
data = SimpleDirectoryReader(input_files=["PATH_TO_PDF.pdf"]).load_data()
index = VectorStoreIndex.from_documents(data)

# Set up memory and chat engine
memory = ChatMemoryBuffer.from_defaults(token_limit=5000)
chat_engine = index.as_chat_engine(
    chat_mode="context",
    llm=llm,
    memory=memory,
    system_prompt="YOUR_SYSTEM_PROMPT"
)

# Chat with the engine
response = chat_engine.chat("YOUR_QUESTION_ABOUT_DOCUMENT")
print(response)
