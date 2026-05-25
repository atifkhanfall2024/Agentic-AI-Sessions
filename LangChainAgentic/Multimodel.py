from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

# from langchain.chat_models import init_chat_model

# model = init_chat_model(model='gemini-3.1-flash-lite-preview' , model_provider='google_genai')

# response = model.invoke('what is ai in 1 line')
# print(response.text)

# from langchain_google_genai import ChatGoogleGenerativeAI
# model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite-preview")
# response = model.invoke('Hi geni how are you')
# print(response.text)


from langchain_groq import ChatGroq
model = ChatGroq(model='llama-3.3-70b-versatile')
response = model.invoke('Hi Groq')
print(response.text)