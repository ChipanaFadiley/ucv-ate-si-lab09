# Pruebas unitarias para la herramienta de evaluación de riesgos.
from travel_assistant.tools.risk_tools import assess_basic_travel_risks


def test_assess_basic_travel_risks_for_cusco():
    # Caso exitoso: Cusco en temporada alta, debería reportar riesgo de altura.
    result = assess_basic_travel_risks("Cusco", "temporada alta")

    assert result["status"] == "success"
    assert len(result["risks"]) >= 1
    assert any("altitude" in risk.lower() or "altura" in risk.lower() for risk in result["risks"])


def test_assess_basic_travel_risks_default_case():
    # Caso exitoso: destino común sin riesgos predefinidos específicos en la herramienta.
    result = assess_basic_travel_risks("Lima", "normal")

    assert result["status"] == "success"
    assert len(result["risks"]) == 1


def test_assess_basic_travel_risks_rainy_season():
    # Caso exitoso: temporada de lluvias, requiere ropa impermeable.
    result = assess_basic_travel_risks("Lima", "temporada de lluvia")
    assert result["status"] == "success"
    assert any(
        "waterproof" in risk.lower() or "lluvia" in risk.lower()
        for risk in result["risks"]
    )

