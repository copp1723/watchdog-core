
import React from 'react';
import { ChartBar } from 'lucide-react';

interface SuggestionChipProps {
  text: string;
  onClick: () => void;
  icon?: React.ReactNode;
}

export const SuggestionChip: React.FC<SuggestionChipProps> = ({ text, onClick, icon = <ChartBar className="h-3.5 w-3.5" /> }) => {
  return (
    <button 
      className="bg-muted/10 hover:bg-muted/20 text-sm px-4 py-2 rounded-full text-foreground transition-all duration-200 flex items-center gap-2 hover:scale-[1.02] border border-muted/20"
      onClick={onClick}
    >
      {icon}
      {text}
    </button>
  );
};
