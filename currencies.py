# pylint: disable-all

# Dictionnaire des taux
# Clés : "FROMTO" (3 lettres source + 3 lettres cible)
# Valeurs : taux float
RATES = {
    "USDEUR": 0.85,
    "CHFEUR": 0.86,
    "GBPEUR": 1.13,
    "EURGBP": 1 / 1.13,  # conversion inverse
}

def convert(amount, currency):
    """Convertit un montant d'une devise vers une autre.

    amount: tuple (valeur, devise_source)
    currency: devise cible (string)
    Retourne le montant converti arrondi, ou None si le taux est inconnu.
    """
    value, from_currency = amount
    key = from_currency + currency
    if key not in RATES:
        return None
    return round(value * RATES[key])
