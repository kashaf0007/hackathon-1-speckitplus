from typing import List, Optional
from openai import OpenAI
from app.core.config import settings

openai_client = OpenAI(api_key=settings.GEMINI_API_KEY)

async def generate_answer(
    query: str,
    context: List[dict], # Changed to List[dict]
    conversation_history: List[dict] = None
) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Answer the user's question ONLY from the provided context. If the answer is not in the context, state that you don't know."},
    ]

    if conversation_history:
        messages.extend(conversation_history)

    # Prepare context for the LLM
    context_str = ""
    sources_list = []
    for i, item in enumerate(context):
        context_str += f"[[{i+1}]] {item['content']}\n"
        sources_list.append(item['source'])

    messages.append({"role": "user", "content": f"Context:\n{context_str}\nQuestion: {query}"})

    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500, # As decided in the spec for max query length, this is a good upper bound for answers
        temperature=0.7,
    )

    answer = response.choices[0].message.content
    
    # Simple grounding check: if the answer explicitly states it doesn't know or cannot find, consider it ungrounded
    if "i don't know" in answer.lower() or "cannot find" in answer.lower():
        # A more sophisticated check would involve verifying if keywords from context are in answer
        return "I apologize, but I cannot find the answer to your question within the provided book content."
    
    # Add sources to the answer
    if sources_list:
        unique_sources = sorted(list(set(sources_list)))
        answer += "\n\nSources: " + ", ".join(unique_sources)
    
    return answer