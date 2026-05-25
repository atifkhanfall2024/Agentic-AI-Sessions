from dotenv import load_dotenv
import os

load_dotenv()

os.environ['Groq_Api_Key'] = os.getenv('Groq_Api_Key')


import langchain
from langchain.agents import create_agent
from langchain_groq import ChatGroq
import requests

print(langchain.__version__)

def get_weather(city: str) -> str:
    """Use this tool whenever the user asks about current weather, temperature, cold, hot, rain, or climate of any city. Input should be only the city name."""

    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    geo_data = requests.get(geo_url, timeout=10).json()

    if "results" not in geo_data:
        return "City not found"

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    weather_data = requests.get(weather_url, timeout=10).json()

    temp = weather_data["current"]["temperature_2m"]

    return f"Current temperature in {city} is {temp}°C"
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="""
You are a weather assistant.
For weather questions, always call get_weather.
Your final answer must be one short sentence.
Do not mention tool, function, API, source, sample, accuracy, or note.
"""
)


response = agent.invoke({"messages":[{"role":"user" , "content":"eid date in peshawar"}]})

print(response["messages"][-1].content)

