from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import requests

# ─── CONFIG ───────────────────────────────────────────────
ANTHROPIC_API_KEY = "your-anthropic-api-key-here"
HUBSPOT_API_KEY = "your-hubspot-api-key-here"

# ─── INITIALISATION DU MODÈLE ─────────────────────────────
# On utilise LangChain pour envelopper Claude
# Avantage vs API directe : gestion native de la mémoire conversationnelle
llm = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    api_key=ANTHROPIC_API_KEY
)

# ─── CONNEXION HUBSPOT ────────────────────────────────────
# Récupère tous les contacts avec leurs propriétés CRM et IA
def get_hubspot_contacts():
    url = "https://api.hubapi.com/crm/v3/objects/contacts"
    headers = {"Authorization": f"Bearer {HUBSPOT_API_KEY}"}
    params = {
        "properties": "firstname,lastname,email,lifecyclestage,hs_lead_status,ai_score,ai_next_action,ai_category",
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# ─── CHARGEMENT DES DONNÉES ───────────────────────────────
print("Chargement des contacts HubSpot...")
contacts_data = get_hubspot_contacts()
contacts_text = str(contacts_data)

# ─── MÉMOIRE CONVERSATIONNELLE ────────────────────────────
# SystemMessage = le rôle et contexte donné à Claude UNE FOIS au départ
# HumanMessage + AIMessage = l'historique qui donne la mémoire
historique = [
    SystemMessage(content=f"""Tu es un assistant CRM expert. 
Tu analyses les données HubSpot et réponds de façon concise aux questions.
Voici les contacts disponibles : {contacts_text}
Réponds uniquement à ce qu'on te demande.""")
]

print("Chatbot CRM prêt. Tape 'quit' pour quitter.\n")

# ─── BOUCLE CONVERSATIONNELLE ─────────────────────────────
# À chaque message, on passe TOUT l'historique à Claude
# C'est ce qui crée la mémoire — Claude voit toute la conversation
while True:
    question = input("Toi: ")
    if question.lower() == "quit":
        break
    
    historique.append(HumanMessage(content=question))
    response = llm.invoke(historique)
    historique.append(AIMessage(content=response.content))
    print(f"Claude: {response.content}\n")