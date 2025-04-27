import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  import.meta.env.VITE_SUPABASE_URL!,
  import.meta.env.VITE_SUPABASE_ANON_KEY!
)

export const subscribeToSalesLogs = (cb: (payload: any) => void) =>
  supabase
    .channel('sales_logs')
    .on(
      'postgres_changes',
      { event: 'INSERT', schema: 'public', table: 'sales_logs' },
      cb
    )
    .subscribe() 