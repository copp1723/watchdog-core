
import React, { useState } from 'react';
import { FileUp, Send, ChartBar, TrendingUp } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Textarea } from '@/components/ui/textarea';
import { InsightCard } from './InsightCard';
import { SuggestionChip } from './SuggestionChip';

export const Chat = () => {
  const [inputValue, setInputValue] = useState('');
  
  const handleInputChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setInputValue(e.target.value);
  };

  const handleSuggestionClick = (question: string) => {
    setInputValue(question);
  };

  const handleFileUpload = async (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (!file) return;

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('/v1/upload', {
        method: 'POST',
        body: formData,
      });
      const json = await response.json();
      console.log('Upload response:', json);
    } catch (error) {
      console.error('Upload error:', error);
    }
  };

  const handleSend = () => {
    if (!inputValue.trim()) return;
    console.log('Sending message:', inputValue);
    setInputValue('');
  };

  return (
    <div className="flex flex-col h-[calc(100vh-8rem)]">
      <div className="flex-1 overflow-y-auto p-6 space-y-8">
        {/* Assistant welcome message */}
        <div className="flex items-start space-x-4 max-w-[85%]">
          <div className="flex-1 bg-[#1E1E1E] rounded-xl p-4 text-foreground">
            <p className="text-base leading-relaxed">How can I help you today?</p>
          </div>
        </div>

        {/* User message */}
        <div className="flex items-start justify-end space-x-4">
          <div className="flex-1 bg-[#252525] rounded-xl p-4 text-foreground ml-auto max-w-[85%]">
            <p className="text-base leading-relaxed">What sales rep sold the highest grossing deal?</p>
          </div>
        </div>

        {/* Assistant message with insight */}
        <div className="flex items-start space-x-4 max-w-[85%]">
          <div className="flex-1 space-y-4">
            <div className="bg-[#1E1E1E] rounded-xl p-4 text-foreground">
              <p className="text-base leading-relaxed">I've analyzed your sales data and found the information about your highest grossing deal:</p>
            </div>
            
            <InsightCard 
              title="Sales Rep with Highest Total Gross"
              employee="Ryan Ouzts"
              employeeTitle="top performing rep"
              amount="$19,923.19"
              percentage="+27%"
              actionItems={[
                "Study Ryan Ouzts's sales strategies for team training.",
                "Analyze their lead source performance for optimization."
              ]}
            />
            
            <div className="flex flex-wrap gap-3 mt-4">
              <SuggestionChip
                text="Show me profit by vehicle type"
                onClick={() => handleSuggestionClick("Show me profit by vehicle type")}
                icon={<ChartBar className="h-3.5 w-3.5" />}
              />
              <SuggestionChip
                text="Which sales rep had the highest profit?"
                onClick={() => handleSuggestionClick("Which sales rep had the highest profit?")}
                icon={<TrendingUp className="h-3.5 w-3.5" />}
              />
            </div>
          </div>
        </div>
      </div>

      {/* Input area */}
      <div className="border-t border-muted bg-background/80 backdrop-blur-xl p-4 fixed bottom-0 left-0 right-0">
        <div className="max-w-chat mx-auto flex items-end gap-3">
          <div>
            <input
              type="file"
              onChange={handleFileUpload}
              className="hidden"
              id="file-upload"
            />
            <label
              htmlFor="file-upload"
              className="inline-flex items-center justify-center rounded-full text-sm bg-muted hover:bg-muted/80 h-10 w-10 cursor-pointer transition-all hover:scale-105"
            >
              <FileUp className="h-5 w-5 text-foreground" />
            </label>
          </div>
          <Textarea
            className="flex-1 bg-secondary-bg border-none text-foreground resize-none rounded-xl placeholder:text-muted-foreground min-h-[44px] py-3 px-4 focus:ring-1 focus:ring-accent/30 transition-all"
            placeholder="Ask any question about your data..."
            rows={1}
            value={inputValue}
            onChange={handleInputChange}
          />
          <Button 
            size="icon" 
            className="rounded-full bg-accent hover:bg-accent/90 transition-all hover:scale-105"
            onClick={handleSend}
            disabled={!inputValue.trim()}
          >
            <Send className="h-5 w-5" />
          </Button>
        </div>
      </div>
    </div>
  );
};
