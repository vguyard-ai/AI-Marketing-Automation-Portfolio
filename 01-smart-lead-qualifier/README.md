# 🧠 Projet #1 — Smart Lead Qualifier

## 📋 Description
Système de qualification automatique des leads entrants via analyse 
sémantique par LLM (Claude API). Le score et les recommandations sont 
injectés automatiquement dans HubSpot en temps réel.

---

## 🎯 Problème Business
Les équipes commerciales perdent du temps à qualifier manuellement 
des leads de qualité variable :
- Priorisation inefficace
- Opportunités à fort potentiel traitées trop tard
- Scoring basé sur des règles rigides (taille, secteur)

---

## ✅ Solution Implémentée

### Flow complet
```
Form HubSpot → Make.com → Claude API → JSON → HubSpot CRM
```

### Ce que l'IA génère
- **Score** : 0 à 100
- **Catégorie** : Cold / Warm / Hot / Very Hot  
- **Action recommandée** : étape concrète pour l'équipe commerciale

---

## 🛠️ Stack
| Outil | Rôle |
|-------|------|
| HubSpot | CRM + formulaire de capture |
| Make.com | Orchestration du workflow |
| Claude API (Anthropic) | Analyse sémantique + scoring |
| JSON | Format d'échange structuré |

---

## 🧠 Logique IA

### Prompt Engineering
Le prompt intègre des règles business précises :
- Le **message** a plus de poids que la taille d'entreprise
- Les messages hors sujet / trolls → score < 20, catégorie Cold
- Le besoin doit être lié au CRM ou marketing automation

### Pourquoi ce choix
Scoring probabiliste (LLM) plutôt que déterministe (IF/THEN) :
- Comprend le langage naturel
- Gère les cas ambigus
- Pas de maintenance de règles manuelles

---

## 🧪 Cas de Tests

| Message | Score | Catégorie | Verdict |
|---------|-------|-----------|---------|
| "Je veux draguer Daisy" | 10 | Cold | ✅ Troll détecté |
| "Nous explorons différentes solutions CRM" | 70 | Warm | ✅ Intention vague |
| "Nous cherchons à structurer notre pipeline B2B" | 80 | Hot | ✅ Intention forte |

---

## 📈 Impact Business
- ✅ Priorisation automatique des leads à fort potentiel
- ✅ Réduction du temps de qualification manuelle
- ✅ Standardisation du scoring
- ✅ Injection directe dans le pipeline CRM

---

## ⚠️ Limites Identifiées
- Dépendance à une API externe (Claude)
- Sensibilité au prompt
- Absence de validation humaine automatique

---

## 🔮 Améliorations Futures
- Modèle hybride : LLM analyse l'intention + règles business (ICP, secteur)
- Intégrer l'historique CRM dans le scoring
- Scoring prédictif basé sur les conversions réelles

---

## 📁 Fichiers
- `README.md` — Documentation complète
- `workflow-make.png` — Screenshot du workflow Make.com
- `hubspot-result.png` — Screenshot du résultat dans HubSpot
- `prompt.md` — Prompt final utilisé

---

## 🔗 Liens
- [Formulaire de test](https://2g00s8.share-eu1.hsforms.com/2vg_D9y1VSpihRfoLxc0-IQ)
- [Portfolio principal](https://github.com/vguyard-ai/AI-Marketing-Automation-Portfolio)
