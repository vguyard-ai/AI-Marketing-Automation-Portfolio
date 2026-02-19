import os
import anthropic
import pandas as pd

# Setup client
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

# Charger les leads
leads = pd.read_csv("leads.csv")

# Fonction génération email
def générer_email(lead):
    prompt = f"""Tu es un expert en marketing B2B. 
Rédige un email de prospection personnalisé et professionnel pour ce lead :

- Prénom : {lead['prenom']}
- Entreprise : {lead['entreprise']}
- Secteur : {lead['secteur']}
- Poste : {lead['poste']}
- Problème principal : {lead['probleme']}

L'email doit :
- Faire 150 mots maximum
- Avoir un objet accrocheur
- Mentionner leur problème spécifique
- Proposer une solution concrète
- Terminer par un CTA clair

Format de réponse :
OBJET : ...
CORPS : ...
"""
    
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return message.content[0].text

# Boucle sur tous les leads
resultats = []

for index, lead in leads.iterrows():
    print(f"Génération email pour {lead['prenom']} {lead['nom']}...")
    email = générer_email(lead)
    resultats.append({
        "prenom": lead['prenom'],
        "nom": lead['nom'],
        "entreprise": lead['entreprise'],
        "email_généré": email
    })

# Export CSV
df_resultats = pd.DataFrame(resultats)
df_resultats.to_csv("emails_générés.csv", index=False)
print("✅ Terminé ! Fichier emails_générés.csv créé.")