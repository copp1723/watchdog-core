
import React from 'react';
import { Moon, Sun, Check } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { Tabs, TabsList, TabsTrigger } from '@/components/ui/tabs';

export const Header = ({ theme, toggleTheme }: { theme: 'light' | 'dark', toggleTheme: () => void }) => {
  return (
    <header className="border-b border-muted bg-background/80 backdrop-blur-xl sticky top-0 z-50 py-3">
      <div className="max-w-chat mx-auto flex flex-col px-6 space-y-2">
        <div className="flex justify-between items-center">
          <div className="flex items-center gap-6">
            <div className="flex items-center gap-3">
              <div className="bg-accent rounded-full w-8 h-8 flex items-center justify-center text-accent-foreground font-semibold">
                W
              </div>
              <div className="flex items-center gap-3">
                <h1 className="text-lg tracking-tight text-foreground">Watchdog AI</h1>
                <div className="bg-success/10 rounded-full px-2.5 py-0.5 flex items-center gap-1 text-xs">
                  <Check className="text-success h-3 w-3" />
                  <span className="text-muted-foreground">342 rows</span>
                </div>
              </div>
            </div>
          </div>
          <Button 
            variant="ghost" 
            size="icon" 
            onClick={toggleTheme}
            className="text-foreground hover:bg-muted transition-colors"
          >
            {theme === 'dark' ? <Sun className="h-5 w-5" /> : <Moon className="h-5 w-5" />}
          </Button>
        </div>
        
        <Tabs defaultValue="insight" className="w-full">
          <TabsList className="bg-muted/50 border border-muted">
            <TabsTrigger 
              value="insight" 
              className="data-[state=active]:bg-accent data-[state=active]:text-accent-foreground hover:bg-muted/30 transition-colors"
            >
              Insight Engine
            </TabsTrigger>
            <TabsTrigger 
              value="connect" 
              disabled 
              className="text-muted-foreground hover:bg-muted/20 transition-colors"
            >
              System Connect
            </TabsTrigger>
          </TabsList>
        </Tabs>
      </div>
    </header>
  );
};
