
import React from 'react';
import { Card } from '@/components/ui/card';
import { BookOpen, ChartBar, User } from 'lucide-react';

interface InsightCardProps {
  title: string;
  employee: string;
  employeeTitle: string;
  amount: string;
  percentage: string;
  actionItems: string[];
}

export const InsightCard = ({
  title,
  employee,
  employeeTitle,
  amount,
  percentage,
  actionItems,
}: InsightCardProps) => {
  return (
    <Card className="bg-[#1E1E1E] border-[#2A2A2A] p-6 space-y-6 rounded-xl">
      <h3 className="text-xl font-semibold text-white">{title}</h3>
      
      <div className="space-y-6">
        <div className="bg-[#252525] rounded-lg p-4">
          <div className="flex items-start gap-4">
            <div className="space-y-1">
              <h4 className="text-[32px] font-semibold text-white tracking-tight">{amount}</h4>
              <p className="text-sm text-gray-400">Total gross</p>
            </div>
            <span className="text-xs bg-success/20 text-success px-2.5 py-1 rounded-full font-medium h-fit">
              {percentage} above team average
            </span>
          </div>
          <div className="flex items-center gap-3 border-t border-[#2A2A2A] mt-4 pt-4">
            <div className="h-10 w-10 rounded-full bg-[#252525] border border-[#2A2A2A] flex items-center justify-center">
              <User className="h-5 w-5 text-white/70" />
            </div>
            <div>
              <p className="text-base text-white font-semibold leading-snug">{employee}</p>
              <p className="text-sm text-gray-400">{employeeTitle}</p>
            </div>
          </div>
        </div>
      </div>

      <div className="space-y-3">
        <h4 className="text-xs font-semibold text-white/90 uppercase tracking-wider">ACTION ITEMS:</h4>
        <div className="bg-[#252525] rounded-lg">
          <div className="space-y-2 p-3">
            {actionItems.map((item, index) => (
              <div 
                key={index}
                className="flex items-center gap-3 p-2 hover:bg-[#2A2A2A] transition-colors cursor-pointer rounded-md"
              >
                <div className="h-8 w-8 rounded-lg bg-[#2A2A2A] flex items-center justify-center">
                  {index === 0 ? (
                    <BookOpen className="h-4 w-4 text-white/70" />
                  ) : (
                    <ChartBar className="h-4 w-4 text-white/70" />
                  )}
                </div>
                <span className="text-sm text-gray-300">
                  {item}
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </Card>
  );
};
