-- Enable Realtime for sales_logs table
alter publication supabase_realtime add table public.sales_logs;

-- Create RLS policy to allow authenticated users to select (read) rows
create policy "realtime select on sales_logs"
  on public.sales_logs
  for select
  using (auth.role() = 'authenticated');

-- Ensure RLS is enabled on the table
alter table public.sales_logs enable row level security; 