# Pruebas unitarias para validar la estructura del sistema multiagente.
from travel_assistant.agent import root_agent


def test_root_agent_name():
    # Verifica que el agente raíz sea el coordinador de viajes.
    assert root_agent.name == "travel_coordinator_agent"


def test_root_agent_has_sub_agents():
    # Verifica que registre los 5 subagentes (los 4 base más el de cultura local del reto).
    assert len(root_agent.sub_agents) == 5


def test_sub_agent_names():
    # Verifica los nombres específicos de los 5 subagentes.
    names = {agent.name for agent in root_agent.sub_agents}

    assert "web_search_agent" in names
    assert "itinerary_agent" in names
    assert "budget_agent" in names
    assert "risk_reviewer_agent" in names
    assert "local_culture_agent" in names  # Verificación del reto.
