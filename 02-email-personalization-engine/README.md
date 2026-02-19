# 📧 Projet #2 - Email Personalization Engine

> Génération automatique d'emails de prospection B2B personnalisés par l'IA

## Problème business

Rédiger des emails de prospection personnalisés pour chaque lead prend un temps considérable. La plupart des équipes envoient des templates génériques qui convertissent mal.

## Solution

Script Python qui lit une liste de leads (CSV) et génère automatiquement un email de prospection ultra-personnalisé pour chacun, adapté au secteur, au poste et à la problématique spécifique du contact.

## Architecture
```
leads.csv → Python Script → Claude API → emails_générés.csv
```

## Stack

- **Python** — Script principal
- **Claude API (Anthropic)** — Génération des emails
- **Pandas** — Lecture/écriture CSV

## Résultats de test

10 emails générés pour 10 secteurs différents :
SaaS, E-commerce, Fintech, Santé, Retail, Logistique, EdTech, Agritech, LegalTech, Médias

Chaque email est personnalisé sur :
- Le prénom et l'entreprise
- Le secteur d'activité
- Le poste du contact
- La problématique spécifique

## Installation
```bash
pip install anthropic pandas
```

## Usage

1. Renseigner votre clé API dans la variable d'environnement `ANTHROPIC_API_KEY`
2. Compléter `leads.csv` avec vos contacts
3. Lancer le script :
```bash
python email_generator.py
```
4. Récupérer les emails générés dans `emails_générés.csv`

## Ce que j'ai appris

- Prompt engineering pour outputs structurés et cohérents
- Boucle sur un dataset avec appels API successifs
- Export de résultats en CSV avec Pandas
