# Pruebas unitarias para la herramienta de cultura local (Reto).
from travel_assistant.tools.culture_tools import get_local_culture_info


def test_get_local_culture_info_for_cusco():
    # Caso Cusco: verifica platos típicos, costumbres andinas y frases quechua.
    result = get_local_culture_info("Cusco")

    assert result["status"] == "success"
    assert "Chiri Uchu" in result["dishes"]
    assert any("Pachamama" in custom for custom in result["customs"])
    assert any("Allianllachu" in phrase for phrase in result["phrases"])


def test_get_local_culture_info_for_buenos_aires():
    # Caso Buenos Aires: verifica asado, mate y frases rioplatenses.
    result = get_local_culture_info("Buenos Aires")

    assert result["status"] == "success"
    assert "Asado" in result["dishes"]
    assert any("mate" in custom.lower() for custom in result["customs"])
    assert any("Che" in phrase for phrase in result["phrases"])


def test_get_local_culture_info_default_case():
    # Caso por defecto: asegura que retorne listas con sugerencias básicas.
    result = get_local_culture_info("Berlin")

    assert result["status"] == "success"
    assert len(result["dishes"]) >= 1
    assert len(result["customs"]) >= 1
    assert len(result["phrases"]) >= 1


def test_get_local_culture_info_for_paris():
    # Caso París: verifica croissants y frases francesas.
    result = get_local_culture_info("Paris")
    assert result["status"] == "success"
    assert "Croissants" in result["dishes"]
    assert any("Bonjour" in phrase for phrase in result["phrases"])


def test_get_local_culture_info_for_arequipa():
    # Caso Arequipa: verifica rocoto relleno y picanterías.
    result = get_local_culture_info("Arequipa")
    assert result["status"] == "success"
    assert "Rocoto Relleno" in result["dishes"]
    assert any("picanterías" in custom for custom in result["customs"])

