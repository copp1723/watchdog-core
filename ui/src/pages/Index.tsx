
import React, { useState, useEffect } from 'react';
import { Header } from '@/components/Header';
import { Chat } from '@/components/Chat';

const Index = () => {
  const [theme, setTheme] = useState<'light' | 'dark'>('dark');

  useEffect(() => {
    const root = document.documentElement;
    if (theme === 'dark') {
      root.classList.add('dark');
    } else {
      root.classList.remove('dark');
    }
  }, [theme]);

  const toggleTheme = () => {
    setTheme(prevTheme => prevTheme === 'dark' ? 'light' : 'dark');
  };

  return (
    <div className="min-h-screen bg-background flex flex-col">
      <Header theme={theme} toggleTheme={toggleTheme} />
      
      {/* Main chat area */}
      <main className="flex-1 flex flex-col relative">
        <div className="max-w-chat mx-auto w-full">
          <Chat />
        </div>
      </main>
    </div>
  );
};

export default Index;
