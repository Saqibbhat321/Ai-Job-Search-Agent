from app.llm.llm_service import LLMService

service = LLMService()

response = service.generate("Hello")

print(response)