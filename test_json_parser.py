from app.llm.llm_service import LLMService
from app.utils.json_parser import JSONParser

service = LLMService()

pprompt = 'Return exactly this JSON: {"name":"Saqib","role":"AI Engineer"}'
response = service.generate(prompt)

print("RAW RESPONSE:")
print(response)

parsed = JSONParser.parse(response)

print("\nPARSED:")
print(parsed)