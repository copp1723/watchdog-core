import React, { Component, ErrorInfo, ReactNode } from 'react';
import { Card } from '@/components/ui/card';
import { AlertTriangle, BookOpen, ChartBar, User } from 'lucide-react';

/**
 * InsightCardProps - Exported interface for component props
 * with explicit types and nullability
 */
export interface InsightCardProps {
  // Core data props
  title?: string | null;
  employee?: string | null;
  employeeTitle?: string | null;
  amount?: string | null;
  percentage?: string | number | null;
  actionItems?: string[] | null;
  // Alternative rendering mode
  rawHtml?: string | null;
}

/**
 * Error boundary component to catch rendering errors
 */
class InsightErrorBoundary extends Component<{ 
  children: ReactNode;
  fallback?: ReactNode;
}> {
  state = { hasError: false, error: null };

  static getDerivedStateFromError(error: Error) {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('[InsightCard] Rendering error:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      // Custom fallback UI
      return this.props.fallback || (
        <Card className="bg-[#1E1E1E] border-[#2A2A2A] p-6 rounded-xl">
          <div className="flex items-center gap-3 text-amber-500">
            <AlertTriangle className="h-5 w-5" />
            <h3 className="text-base font-medium">Insight unavailable</h3>
          </div>
          <p className="text-sm text-gray-400 mt-2">
            There was an error displaying this insight. Please try refreshing the page.
          </p>
        </Card>
      );
    }

    return this.props.children;
  }
}

/**
 * Core InsightCard component implementation
 */
const InsightCard = ({
  title = "Insight",
  employee = "",
  employeeTitle = "",
  amount = "",
  percentage = "",
  actionItems = [],
  rawHtml = ""
}: InsightCardProps) => {
  // Debug logging for all incoming props
  console.debug('[InsightCard] Rendering with props:', {
    title, employee, employeeTitle, amount, percentage, 
    actionItemsCount: actionItems?.length ?? 0,
    hasRawHtml: !!rawHtml
  });

  // Normalize values to handle null/undefined properly
  const safeTitle = title ?? "Insight";
  const safeEmployee = employee ?? "";
  const safeEmployeeTitle = employeeTitle ?? "";
  const safeAmount = amount ?? "";
  const safeActionItems = actionItems ?? [];
  
  // Handle percentage display specially
  let displayPercentage = "";
  if (percentage !== null && percentage !== undefined) {
    // Convert number to string with % if needed
    if (typeof percentage === 'number') {
      // For zero, show "0 %"
      if (percentage === 0) {
        displayPercentage = "0 %";
      } 
      // For positive/negative values, format properly
      else {
        const sign = percentage > 0 ? '+' : '';
        displayPercentage = `${sign}${percentage}%`;  
      }
    } else {
      // Handle string values, assuming they might already have % sign
      displayPercentage = percentage.includes('%') ? percentage : `${percentage}%`;
    }
  } else {
    // For null/undefined, use em dash
    displayPercentage = "—";
  }

  // Helper to render content - this enables a cleaner conditional approach
  const renderContent = () => {
    // Handle raw HTML case
    if (rawHtml) {
      return (
        <Card className="bg-[#1E1E1E] border-[#2A2A2A] p-6 rounded-xl">
          <div dangerouslySetInnerHTML={{ __html: rawHtml }} />
        </Card>
      );
    }

    // Structured data rendering with conditional sections
    return (
      <Card className="bg-[#1E1E1E] border-[#2A2A2A] p-6 space-y-6 rounded-xl">
        {/* Title is always shown, with fallback already applied */}
        <h3 className="text-xl font-semibold text-white">{safeTitle}</h3>
        
        {/* Financial metrics section - only shown if we have amount or percentage */}
        {(safeAmount || displayPercentage) && (
          <div className="space-y-6">
            <div className="bg-[#252525] rounded-lg p-4">
              <div className="flex items-start gap-4">
                {safeAmount && (
                  <div className="space-y-1">
                    <h4 className="text-[32px] font-semibold text-white tracking-tight">{safeAmount}</h4>
                    <p className="text-sm text-gray-400">Total gross</p>
                  </div>
                )}
                
                {displayPercentage && (
                  <span className="text-xs bg-success/20 text-success px-2.5 py-1 rounded-full font-medium h-fit">
                    {displayPercentage} above team average
                  </span>
                )}
              </div>
              
              {/* Employee section - only shown if we have employee data */}
              {safeEmployee && (
                <div className="flex items-center gap-3 border-t border-[#2A2A2A] mt-4 pt-4">
                  <div className="h-10 w-10 rounded-full bg-[#252525] border border-[#2A2A2A] flex items-center justify-center">
                    <User className="h-5 w-5 text-white/70" />
                  </div>
                  <div>
                    <p className="text-base text-white font-semibold leading-snug">{safeEmployee}</p>
                    {safeEmployeeTitle && <p className="text-sm text-gray-400">{safeEmployeeTitle}</p>}
                  </div>
                </div>
              )}
            </div>
          </div>
        )}

        {/* Action items section - only shown if we have action items */}
        {safeActionItems.length > 0 && (
          <div className="space-y-3">
            <h4 className="text-xs font-semibold text-white/90 uppercase tracking-wider">ACTION ITEMS:</h4>
            <div className="bg-[#252525] rounded-lg">
              <div className="space-y-2 p-3">
                {safeActionItems.map((item, index) => (
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
        )}
      </Card>
    );
  };

  // Render the component with proper error boundaries
  try {
    return renderContent();
  } catch (error) {
    console.error('[InsightCard] Error in render function:', error);
    // Provide a minimal fallback in case the error boundary isn't in place
    return (
      <Card className="bg-[#1E1E1E] border-[#2A2A2A] p-6 rounded-xl">
        <div className="text-amber-500">Error rendering insight</div>
      </Card>
    );
  }
};

/**
 * Wrapped component with error boundary
 * This is the default export that should be used by consumers
 */
export default function InsightCardWithBoundary(props: InsightCardProps) {
  return (
    <InsightErrorBoundary>
      <InsightCard {...props} />
    </InsightErrorBoundary>
  );
}

/**
 * Export the unwrapped component as a named export for backward compatibility
 */
export { InsightCard };
