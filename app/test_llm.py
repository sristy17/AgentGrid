from app.services.llm_service import LLMService

llm = LLMService()

result = llm.generate_json("""
Return:
{
  "message": "hello"
}
""")

print(result)