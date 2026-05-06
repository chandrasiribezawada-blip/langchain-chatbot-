from langchain_community.llms import Ollama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

# Load local model (make sure you installed it via ollama pull)
llm = Ollama(model="llama3")

# Memory
memory = ConversationBufferMemory()

# Conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory
)

def chat_with_bot(user_input):
    response = conversation.run(user_input)
    return response
