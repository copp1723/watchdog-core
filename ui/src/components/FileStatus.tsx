
import React from 'react';
import { Check } from 'lucide-react';

interface FileStatusProps {
  fileName: string;
  rowCount: number;
}

export const FileStatus: React.FC<FileStatusProps> = ({ fileName, rowCount }) => {
  return (
    <div className="bg-success/10 rounded-full px-3 py-1 flex items-center gap-1.5 text-xs">
      <Check className="text-success h-3.5 w-3.5" />
      <span className="text-muted-foreground">
        {rowCount.toLocaleString()} rows
      </span>
    </div>
  );
};
