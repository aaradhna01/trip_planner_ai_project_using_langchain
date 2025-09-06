# planner_chain.py
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
llm = ChatOpenAI(temperature=0.7, model_name="gpt-4")

template = """
You are a smart travel planner. Generate a travel plan based on:
From City: {from_city}
To City: {to_city}
Departure: {departure}
Return: {return_date}
Interests: {interests}

Give a day-wise itinerary with helpful tips, travel suggestions, and food recommendations.
"""

prompt = PromptTemplate(
    input_variables=["from_city", "to_city", "departure", "return_date", "interests"],
    template=template
)

trip_chain = LLMChain(llm=llm, prompt=prompt)
