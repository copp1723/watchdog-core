
import React from 'react';
import { Tabs, TabsList, TabsTrigger } from '@/components/ui/tabs';

export const NavigationTabs = () => {
  return (
    <div className="border-b border-muted bg-background/50 backdrop-blur-xl">
      <div className="max-w-chat mx-auto px-6 py-2">
        <Tabs defaultValue="insight" className="w-full">
          <TabsList className="bg-muted/50 border border-muted">
            <TabsTrigger value="insight" className="data-[state=active]:bg-accent data-[state=active]:text-accent-foreground">
              Insight Engine
            </TabsTrigger>
            <TabsTrigger value="connect" disabled className="text-muted-foreground">
              System Connect
            </TabsTrigger>
          </TabsList>
        </Tabs>
      </div>
    </div>
  );
};
