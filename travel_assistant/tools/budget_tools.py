# Herramienta para estimar el presupuesto del viaje en base al destino, días y presupuesto diario.
def estimate_trip_budget(destination: str, days: int, daily_budget_usd: float) -> dict:
    """Estimate a basic travel budget.

    Args:
        destination: Travel destination.
        days: Number of travel days.
        daily_budget_usd: Estimated budget per day in US dollars.

    Returns:
        Dictionary with budget calculation details.
    """
    # Validación: los días deben ser mayores a cero.
    if days <= 0:
        return {
            "status": "error",
            "message": "The number of days must be greater than zero.",
        }

    # Validación: el presupuesto diario debe ser mayor a cero.
    if daily_budget_usd <= 0:
        return {
            "status": "error",
            "message": "The daily budget must be greater than zero.",
        }

    # Cálculo del presupuesto total estimado.
    total = days * daily_budget_usd

    return {
        "status": "success",
        "destination": destination,
        "days": days,
        "daily_budget_usd": daily_budget_usd,
        "estimated_total_usd": total,
    }
