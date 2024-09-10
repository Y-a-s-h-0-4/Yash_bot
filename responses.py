from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Initialize the model
model = OllamaLLM(model="llama3.1")

# Template for the prompt
template = (
    "You are tasked with generating a conversational response based on the following user input: {user_input}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Generate Response:** Provide a response that directly matches the context of the user input. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Direct Response Only:** Your output should contain only the response to the user input, and answer it creatively."
)

def get_response(user_input: str) -> str:
    # Create the prompt template
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model

    # Invoke the model with the user input
    response = chain.invoke({"user_input": user_input})

    return response.strip()  # Remove any extra whitespace