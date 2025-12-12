export async function queryChatbot(query: string, conversationId: string | null, apiBaseUrl: string, apiKey: string) {
  const response = await fetch(`${apiBaseUrl}/query`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-API-Key': apiKey,
    },
    body: JSON.stringify({ query, conversation_id: conversationId }),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Failed to query chatbot');
  }

  return response.json();
}

export async function querySelectedTextChatbot(query: string, text: string, conversationId: string | null, apiBaseUrl: string, apiKey: string) {
  const response = await fetch(`${apiBaseUrl}/selected-text`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-API-Key': apiKey,
    },
    body: JSON.stringify({ query, text, conversation_id: conversationId }),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Failed to query selected text chatbot');
  }

  return response.json();
}