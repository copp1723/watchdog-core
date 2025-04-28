import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  import.meta.env.VITE_SUPABASE_URL || '',
  import.meta.env.VITE_SUPABASE_ANON_KEY || ''
)

// Validate that environment variables are provided
if (!import.meta.env.VITE_SUPABASE_URL || !import.meta.env.VITE_SUPABASE_ANON_KEY) {
  console.error('Missing Supabase environment variables. Real-time functionality may not work correctly.');
}

export const subscribeToSalesLogs = (cb: (payload: any) => void) =>
  supabase
    .channel('sales_logs')
    .on(
      'postgres_changes',
      { event: 'INSERT', schema: 'public', table: 'sales_logs' },
      cb
    )
    .subscribe() 