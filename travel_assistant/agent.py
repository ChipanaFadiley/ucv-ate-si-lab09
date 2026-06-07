# Punto de entrada principal para Google ADK. Define la variable root_agent.
from travel_assistant.agents.coordinator import travel_coordinator_agent

# El agente raíz del sistema es el coordinador de viajes.
root_agent = travel_coordinator_agent
