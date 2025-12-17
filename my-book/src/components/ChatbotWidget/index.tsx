import React, { useState, useRef, useEffect } from 'react';
import { queryChatbot, querySelectedTextChatbot } from '../../services/chatbot';
import styles from './ChatbotWidget.module.css';

const ChatbotWidget: React.FC = () => {
  const [isOpen, setIsOpen] = useState(true);
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<{ role: string; content: string; sources?: string[] }[]>([]);
  const [loading, setLoading] = useState(false);
  const [conversationId, setConversationId] = useState<string | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e: React.FormEvent) => {
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

  // The handleSelectedTextQuery function can be kept for future use or removed if not needed.
  // For now, it's not connected to any UI element in the new design.
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
    <>
      {/* Chat Panel */}
      <div
        className={`${styles.chatPanel} ${isOpen ? styles.chatPanelOpen : ''}`}
        style={{ zIndex: 1000 }}
      >
        {/* Header */}
        <div className="flex justify-between items-center p-4 bg-gray-800 text-white">
          <h3 className="text-lg font-semibold">RAG Chatbot</h3>
          <button onClick={() => setIsOpen(false)} className="text-white hover:text-gray-300">
            &times;
          </button>
        </div>

        {/* Messages Area */}
        <div className="flex-1 p-4 overflow-y-auto">
          {messages.map((msg, index) => (
            <div key={index} className={`mb-3 p-3 rounded-lg ${msg.role === 'user' ? 'bg-blue-100 text-right' : 'bg-gray-100'}`}>
              <div className="font-bold capitalize">{msg.role}</div>
              <div>{msg.content}</div>
              {msg.sources && msg.sources.length > 0 && (
                <div className="text-xs text-gray-500 mt-1">
                  Sources: {msg.sources.join(', ')}
                </div>
              )}
            </div>
          ))}
          {loading && <div className="text-gray-500">Typing...</div>}
          <div ref={messagesEndRef} />
        </div>

        {/* Input Form */}
        <form onSubmit={handleSubmit} className="p-4 border-t border-gray-200">
          <div className="flex">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask a question..."
              disabled={loading}
              className="flex-grow px-3 py-2 border border-gray-300 rounded-l-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <button
              type="submit"
              disabled={loading}
              className="px-4 py-2 bg-blue-500 text-white rounded-r-md hover:bg-blue-600 disabled:bg-gray-400"
            >
              Send
            </button>
          </div>
        </form>
      </div>

      {/* Chat Button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className={styles.chatbotButton}
        style={{ zIndex: 1001 }}
      >
        <svg xmlns="http://www.w3.org/2000/svg" className="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
        </svg>
      </button>
    </>
  );
};

export default ChatbotWidget;
