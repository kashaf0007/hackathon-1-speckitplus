const API_BASE_URL = 'https://kashafaman123-hackathon-1.hf.space'; 

export async function queryChatbot(query, conversationId = null) {
  try {
    const response = await fetch(`${API_BASE_URL}/query`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query, conversation_id: conversationId }),
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({ detail: 'Failed to query chatbot' }));
      return { error: errorData.detail };
    }

    return response.json();
  } catch (error) {
    return { error: 'Failed to connect to the chatbot service.' };
  }
}

export async function querySelectedTextChatbot(query, text, conversationId = null) {
  try {
    const response = await fetch(`${API_BASE_URL}/selected-text`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query, text, conversation_id: conversationId }),
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({ detail: 'Failed to query selected text chatbot' }));
      return { error: errorData.detail };
    }

    return response.json();
  } catch (error) {
    return { error: 'Failed to connect to the chatbot service.' };
  }
}
