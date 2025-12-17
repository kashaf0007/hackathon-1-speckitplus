from typing import List, Optional
import google.generativeai as genai
from app.core.config import settings

# Configure Google Gemini
genai.configure(api_key=settings.gemini_api_key)
model = genai.GenerativeModel(settings.gemini_model)

async def generate_answer(
    query: str,
    context: List[dict],
    conversation_history: List[dict] = None
) -> str:
    # Prepare context for the LLM
    context_str = ""
    sources_list = []
    for i, item in enumerate(context):
        context_str += f"[[{i+1}]] {item['content']}\n"
        sources_list.append(item['source'])

    # Build the prompt
    system_instruction = "You are a helpful assistant. Answer the user's question ONLY from the provided context. If the answer is not in the context, state that you don't know."

    prompt = f"{system_instruction}\n\nContext:\n{context_str}\n\nQuestion: {query}"

    # Add conversation history if available
    if conversation_history:
        history_str = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation_history])
        prompt = f"{system_instruction}\n\nConversation History:\n{history_str}\n\nContext:\n{context_str}\n\nQuestion: {query}"

    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            max_output_tokens=500,
            temperature=0.7,
        )
    )

    answer = response.text

    # Simple grounding check: if the answer explicitly states it doesn't know or cannot find, consider it ungrounded
    if "i don't know" in answer.lower() or "cannot find" in answer.lower():
        return "I apologize, but I cannot find the answer to your question within the provided book content."

    # Add sources to the answer
    if sources_list:
        unique_sources = sorted(list(set(sources_list)))
        answer += "\n\nSources: " + ", ".join(unique_sources)

    return answer