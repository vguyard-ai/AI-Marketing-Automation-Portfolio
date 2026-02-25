# 🤖 Chatbot CRM — Projet #5

## Description
Assistant conversationnel connecté à HubSpot via LangChain et Claude AI.
Permet d'interroger ses contacts CRM en langage naturel avec mémoire conversationnelle.

## Ce que ça fait
- Récupère automatiquement tous les contacts HubSpot
- Répond à des questions en langage naturel sur les leads
- Garde la mémoire de toute la conversation
- Analyse les AI Scores, catégories et prochaines actions

## Exemples de questions
- "Combien de contacts j'ai en tout ?"
- "Qui a le meilleur AI Score ?"
- "Quelle est la prochaine action pour Thomas Bernard ?"
- "Montre-moi tous les leads Hot"

## Stack technique
- Python 3.11+
- LangChain + langchain-anthropic
- Claude Sonnet (Anthropic API)
- HubSpot CRM API v3

## Installation
```bash
pip install langchain langchain-anthropic requests
```

## Configuration
Remplacer dans `chatbot_crm.py` :
- `ANTHROPIC_API_KEY` → ta clé Anthropic
- `HUBSPOT_API_KEY` → ton token HubSpot Private App

## Lancer le chatbot
```bash
python chatbot_crm.py
```