# Designer bot
## Prepares the information from Journalist_bot in order to send it to Towncrier_bot

class Designer:
    def __init__(self):
        pass

    def dailyMessage(self, data):
        return [f"""
*Rapport Quotidien des Conditions*
_{data['info_time']}_
Conditions:
    - Surface: {data['conditions']['surface']}
    - Base: {data['conditions']['base']}
    - Couverture: {data['conditions']['couverture']}

Pistes: {data['pistes']['ouvert']}/{data['pistes']['index']}
Remontées: {data['remontees']['ouvert']}/{data['remontees']['index']}
Chalets: {data['chalets']['ouvert']}/{data['chalets']['index']}""",
        f"`{data['conditions']['message']}`"]
    
    def statutMessage(self, data, query):
        if query == "piste":
            dictionnary = data["pistes"]
        elif query == "remontee":
            dictionnary = data["remontees"]
        elif query == "chalet":
            dictionnary = data["chalets"]
        else:
            return "Rien."

        ouvert = ", ".join(dictionnary["statut"]["ouvert"])
        ferme = ", ".join(dictionnary["statut"]["ferme"])
        return f"""
Ouvert: {ouvert}
`Fermé: {ferme}`"""