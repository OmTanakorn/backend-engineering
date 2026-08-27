-- Runs once, when the pgdata volume is first created.

-- Phase 2: find the slowest queries in the system.
--   SELECT query, calls, mean_exec_time, rows
--   FROM pg_stat_statements ORDER BY mean_exec_time DESC LIMIT 10;
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Inspect index usage and bloat while tuning.
CREATE EXTENSION IF NOT EXISTS pgstattuple;

-- Trigram indexes (GIN/GiST practice).
CREATE EXTENSION IF NOT EXISTS pg_trgm;
