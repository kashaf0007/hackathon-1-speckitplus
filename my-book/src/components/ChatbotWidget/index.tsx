import React, { useState } from 'react';
import styles from './ChatbotWidget.module.css';

const ChatbotWidget: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  return (
    <>
      <button className={styles.chatbotButton} onClick={toggleChat}>
        Chat
      </button>
      <div className={`${styles.chatPanel} ${isOpen ? styles.chatPanelOpen : ''}`}>
        <div className={styles.chatPanelHeader}>
          <span>RAG Chatbot</span>
          <button onClick={toggleChat}>X</button>
        </div>
        <div className={styles.chatPanelBody}>
          {/* Chat content will go here */}
          <p>Hello! How can I help you today?</p>
        </div>
      </div>
    </>
  );
};

export default ChatbotWidget;