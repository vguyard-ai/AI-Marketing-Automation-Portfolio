from langchain_anthropic import ChatAnthropic
from langchain_core.messages import HumanMessage, AIMessage

llm = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    api_key="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"
)

# Historique de conversation
historique = []

# Message 1
historique.append(HumanMessage(content="Mon lead principal s'appelle Marc, budget 50k€"))
response1 = llm.invoke(historique)
historique.append(AIMessage(content=response1.content))
print("Claude:", response1.content)

# Message 2 - est-ce qu'il se souvient ?
historique.append(HumanMessage(content="Quel est son budget ?"))
response2 = llm.invoke(historique)
print("Claude:", response2.content)