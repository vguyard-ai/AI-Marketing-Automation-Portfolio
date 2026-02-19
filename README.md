# 🤖 AI Marketing Automation Portfolio

> CRM & Marketing Automation Specialist transitioning to AI Agents & Workflow Optimization

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Victor_Guyard-blue?style=flat&logo=linkedin)](https://linkedin.com/in/ton-profil)
[![Claude AI](https://img.shields.io/badge/Claude_AI-Anthropic-orange?style=flat)](https://anthropic.com)
[![HubSpot](https://img.shields.io/badge/HubSpot-CRM-red?style=flat)](https://hubspot.com)

---

## 👋 À propos

3,5 ans d'expérience en CRM & Marketing Automation (HubSpot, Intercom).
En transition vers l'**AI Marketing Automation** : agents IA, workflows intelligents, intégration LLM dans les processus CRM.

**Disponible : Mars 2026 | Paris/IDF | Hybride**

---

## 🚀 Projets IA

| # | Projet | Stack | Statut |
|---|--------|-------|--------|
| 01 | [🧠 Smart Lead Qualifier](#projet-1--smart-lead-qualifier) | HubSpot • Make.com • Claude API | ✅ Terminé |
| 02 | 📧 Email Personalization Engine | Python • Claude API • HubSpot | ✅ Terminé |
| 03 | 🎯 Multi-Channel Campaign Automator | Make.com • Claude API • HubSpot | ✅ Terminé |
| 04 | 🤖 Chatbot CRM | LangChain • Claude API • HubSpot | ⏳ À venir |
| 05 | 🔨 Email Agent | LangChain • SendGrid • HubSpot | ⏳ À venir |
| 06 | 🧠 Marketing Knowledge Base (RAG) | LangChain • ChromaDB • Claude API | ⏳ À venir |
| 07 | 🎛️ Real-Time Marketing Command Center | Make.com • Slack • Google Sheets | ⏳ À venir |

---

## 🔍 Projet 1 : Smart Lead Qualifier

> Qualification automatique des leads entrants via analyse sémantique par LLM

### Problème business
Les équipes commerciales perdent du temps à qualifier manuellement des leads de qualité variable. La priorisation est inefficace et les opportunités à fort potentiel sont traitées trop tard.

### Solution
Workflow automatisé qui analyse le message du lead en langage naturel et génère :
- Un **score de qualification** (0–100)
- Une **catégorie** (Cold / Warm / Hot / Very Hot)
- Une **action commerciale recommandée**

Le tout injecté automatiquement dans HubSpot en temps réel.

### Architecture
```
Form HubSpot → Make.com → Claude API → JSON Score → HubSpot CRM
```

### Stack
- **HubSpot** — CRM & formulaire
- **Make.com** — Orchestration du workflow
- **Claude API (Anthropic)** — Analyse sémantique
- **JSON** — Format d'échange structuré

### Résultats de test
| Message | Score | Catégorie |
|---------|-------|-----------|
| "Je veux draguer Daisy" | 8 | Cold ✅ |
| "Nous explorons différentes solutions CRM" | 70 | Warm ✅ |
| "Budget validé pour implémenter un CRM IA" | 80 | Hot ✅ |

### Ce que j'ai appris
- Intégration d'un LLM dans un workflow no-code
- Prompt engineering pour output JSON structuré
- Gestion des cas limites (trolls, messages hors sujet)
- Injection automatique de données dans un CRM

---

## 🛠️ Stack Technique

**IA & LLM**
- Claude API (Anthropic)
- LangChain
- Prompt Engineering
- RAG (Retrieval Augmented Generation)

**CRM & Automation**
- HubSpot (Marketing + Sales Hub)
- Make.com
- API Integration

**Dev**
- Python
- JSON
- Git/GitHub

---

## 📫 Contact

- **Email** : v.guyarddechalambert@gmail.com
- **LinkedIn** : [linkedin.com/in/ton-profil](https://linkedin.com)
- **Disponibilité** : Mars 2026
