import React, { useState } from 'react';
import { queryChatbot, querySelectedTextChatbot } from '../../services/chatbot';

function ChatbotWidget() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [conversationId, setConversationId] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = { role: 'user', content: input };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setLoading(true);
    setInput('');

    try {
      const response = await queryChatbot(input, conversationId);
      const botMessage = { role: 'assistant', content: response.answer, sources: response.sources };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
      setConversationId(response.conversation_id);
    } catch (error) {
      console.error('Chatbot error:', error);
      setMessages((prevMessages) => [...prevMessages, { role: 'assistant', content: 'Error: Could not get a response.' }]);
    } finally {
      setLoading(false);
    }
  };

  const handleSelectedTextQuery = async () => {
    const selectedText = "The quick brown fox jumps over the lazy dog."; // Placeholder for selected text
    const query = "What is the meaning of this text?"; // Placeholder query for selected text
    
    if (!selectedText.trim()) return;

    const userMessage = { role: 'user', content: `Query about selected text: "${selectedText}" - ${query}` };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setLoading(true);

    try {
      const response = await querySelectedTextChatbot(query, selectedText, conversationId);
      const botMessage = { role: 'assistant', content: response.answer, sources: response.sources };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
      setConversationId(response.conversation_id);
    } catch (error) {
      console.error('Chatbot error:', error);
      setMessages((prevMessages) => [...prevMessages, { role: 'assistant', content: 'Error: Could not get a response from selected text query.' }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{
      border: '1px solid #ccc',
      borderRadius: '8px',
      padding: '16px',
      maxWidth: '400px',
      margin: '20px',
      backgroundColor: '#f9f9f9',
      fontFamily: 'Arial, sans-serif'
    }}>
      <h3 style={{ marginTop: 0, color: '#333' }}>RAG Chatbot</h3>
      <div style={{
        height: '300px',
        overflowY: 'auto',
        border: '1px solid #eee',
        padding: '8px',
        marginBottom: '16px',
        backgroundColor: '#fff'
      }}>
        {messages.map((msg, index) => (
          <div key={index} style={{ marginBottom: '8px' }}>
            <strong style={{ color: msg.role === 'user' ? '#007bff' : '#28a745' }}>{msg.role}: </strong>
            <span>{msg.content}</span>
            {msg.sources && msg.sources.length > 0 && (
              <div style={{ fontSize: '0.8em', color: '#666' }}>
                (Sources: {msg.sources.join(', ')})
              </div>
            )}
          </div>
        ))}
        {loading && <div style={{ color: '#6c757d' }}>Typing...</div>}
      </div>
      <form onSubmit={handleSubmit} style={{ display: 'flex', marginBottom: '8px' }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question..."
          disabled={loading}
          style={{
            flexGrow: 1,
            padding: '8px',
            border: '1px solid #ccc',
            borderRadius: '4px',
            marginRight: '8px'
          }}
        />
        <button
          type="submit"
          disabled={loading}
          style={{
            padding: '8px 12px',
            backgroundColor: '#007bff',
            color: 'white',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer'
          }}
        >
          Send
        </button>
      </form>
      <button
        onClick={handleSelectedTextQuery}
        disabled={loading}
        style={{
          width: '100%',
          padding: '8px 12px',
          backgroundColor: '#6c757d',
          color: 'white',
          border: 'none',
          borderRadius: '4px',
          cursor: 'pointer'
        }}
      >
        Query Selected Text (Placeholder)
      </button>
    </div>
  );
}

export default ChatbotWidget;
