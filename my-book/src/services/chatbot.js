const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000'; // Replace with Docusaurus env var

export async function queryChatbot(query, conversationId = null) {
  const response = await fetch(`${API_BASE_URL}/query`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-API-Key': process.env.REACT_APP_API_KEY, // Replace with Docusaurus env var
    },
    body: JSON.stringify({ query, conversation_id: conversationId }),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Failed to query chatbot');
  }

  return response.json();
}

export async function querySelectedTextChatbot(query, text, conversationId = null) {
  const response = await fetch(`${API_BASE_URL}/selected-text`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-API-Key': process.env.REACT_APP_API_KEY, // Replace with Docusaurus env var
    },
    body: JSON.stringify({ query, text, conversation_id: conversationId }),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Failed to query selected text chatbot');
  }

  return response.json();
}
