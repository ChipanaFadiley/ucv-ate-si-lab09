# Agente de cultura local (Reto del Laboratorio) que recomienda platos, costumbres y frases.
from google.adk.agents import Agent

from travel_assistant.tools.culture_tools import get_local_culture_info

local_culture_agent = Agent(
    name="local_culture_agent",
    model="gemini-2.0-flash",
    description="Provides recommendations on local culture, typical dishes, customs and phrases.",
    instruction="""
You are a local culture agent.

Your task is to recommend typical dishes, explain local customs, and suggest useful phrases.
Use the available tool when the destination is provided.

Rules:
1. Recomendar platos típicos del destino.
2. Explicar costumbres locales importantes.
3. Sugerir frases útiles para el viajero.
4. Keep the style friendly and informative.
""",
    tools=[get_local_culture_info],  # Herramienta personalizada de cultura.
)
