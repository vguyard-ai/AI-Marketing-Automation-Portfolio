# 🎯 Projet #3 - Multi-Channel Campaign Automator

> Qualification et routage automatique des leads par persona via IA

## Problème business

Chaque lead a un profil différent et nécessite une approche commerciale adaptée. 
Traiter tous les leads de la même façon fait perdre des opportunités et du temps.

## Solution

Workflow Make.com qui analyse automatiquement le message d'un lead, 
détermine son profil (Hot/Warm/Cold) via Claude AI, et met à jour 
HubSpot en conséquence en temps réel.

## Architecture
```
HubSpot Form → Make.com → Claude API → JSON Parse → HubSpot Search → Router → Update Contact
```

## Stack

- **HubSpot** — CRM, formulaire & mise à jour contacts
- **Make.com** — Orchestration du workflow
- **Claude API** — Analyse du message et classification du lead
- **JSON** — Format d'échange structuré

## Workflow

1. Lead soumet le formulaire HubSpot
2. Make.com déclenche le scénario
3. Claude analyse le message et retourne Hot/Warm/Cold
4. Le Router dirige vers la bonne branche
5. HubSpot est mis à jour avec la catégorie

## Ce que j'ai appris

- Architecture Router dans Make.com
- Filtrage par email pour cibler un contact unique
- Prompt engineering pour classification structurée
- Débogage de workflows no-code