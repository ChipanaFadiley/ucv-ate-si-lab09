# Herramienta para obtener información de cultura local: platos típicos, costumbres y frases.
def get_local_culture_info(destination: str) -> dict:
    """Return local culture information: typical dishes, customs, and useful phrases.

    Args:
        destination: Travel destination.

    Returns:
        Dictionary with culture details.
    """
    # Normalización del destino para búsquedas sencillas.
    destination_normalized = destination.lower().strip()

    dishes = []
    customs = []
    phrases = []

    if "cusco" in destination_normalized or "machu picchu" in destination_normalized:
        dishes = ["Chiri Uchu", "Cuy Chactado", "Trucha Frita"]
        customs = [
            "Greeting people with respect and asking permission before taking photos",
            "Paying tribute to Pachamama (Mother Earth) is a deep-seated tradition"
        ]
        phrases = [
            "Allianllachu (Quechua for 'How are you?')",
            "Sulpayki (Quechua for 'Thank you')"
        ]
    elif "buenos aires" in destination_normalized or "argentina" in destination_normalized:
        dishes = ["Asado", "Empanadas de carne", "Alfajores con dulce de leche"]
        customs = [
            "Sharing mate is a social custom representing friendship",
            "Greeting with a single cheek kiss between friends"
        ]
        phrases = [
            "¿Cómo andás? (How are you?)",
            "Che (Hey/Friend)",
            "Muchas gracias (Thank you very much)"
        ]
    elif (
        "paris" in destination_normalized
        or "parís" in destination_normalized
        or "france" in destination_normalized
        or "francia" in destination_normalized
    ):
        dishes = ["Croissants", "Coq au vin", "Escargots de Bourgogne", "Macarons"]
        customs = [
            "Always greet with 'Bonjour' or 'Bonsoir' when entering shops",
            "Keeping voice volume low in restaurants and public spaces"
        ]
        phrases = [
            "Bonjour (Good morning/Hello)",
            "Merci beaucoup (Thank you very much)",
            "S'il vous plaît (Please)"
        ]
    elif "arequipa" in destination_normalized:
        dishes = ["Rocoto Relleno", "Adobo Arequipeño", "Solterito de Queso"]
        customs = [
            "Visiting traditional 'picanterías' (traditional restaurants)",
            "Very proud of their local identity and historical heritage"
        ]
        phrases = [
            "¡Qué de primera! (Excellent / Great!)",
            "Muchas gracias (Thank you)"
        ]
    else:
        dishes = ["Typical local dishes and street foods"]
        customs = ["Respect local traditions and dress codes for religious or sacred sites"]
        phrases = ["Hola (Hello)", "Gracias (Thank you)", "Por favor (Please)"]

    return {
        "status": "success",
        "destination": destination,
        "dishes": dishes,
        "customs": customs,
        "phrases": phrases
    }
