# Watchdog Core

Watchdog AI converts dealership sales logs into instant insights via LLMs.

## Overview

Watchdog Core is the backend engine that powers our AI-driven analytics platform for automotive dealerships. The system ingests sales log data, processes it using advanced language models, and generates actionable insights for dealership management teams.

## Key Features

- Automated sales log parsing and normalization
- AI-powered trend identification and analysis
- Real-time performance metrics and recommendations
- Secure multi-tenant architecture

## Project Structure

- `api/`: FastAPI service
- `ui/`: React frontend (Lovable-generated)
- `interfaces/`: Pure-python ports/adapters
- `infra/`: Infrastructure as Code
- `.github/`: CI workflows
- `scripts/`: One-off utilities
- `tests/`: Test suite

## Definition of Done

For all feature work, the following checklist must be satisfied:

- [ ] Build passes CI (lint + mypy + pytest)
- [ ] Sentry traces present in staging
- [ ] /metrics endpoint returns data

## Getting Started

*Coming soon*

## License

*Proprietary*

