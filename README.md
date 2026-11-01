# genpark-agentic-commerce-saas-magic-number-cac-payback-unit-economics-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

Enterprise SaaS Magic Number, CAC Payback Period (months), LTV:CAC and gross margin burn multiple evaluator.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `evaluate_saas_unit_economics`
- **Category**: `agentic_commerce`

### Method Documentation
Evaluate B2B Enterprise SaaS sales efficiency, CAC Payback Period (months), Magic Number, and LTV:CAC ratio.
Magic Number = (Quarterly Net ARR Growth * 4) / Prior Quarter Sales & Marketing Expense.
Benchmarks go-to-market capital efficiency against top-quartile Bessemer SaaS metrics.

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "evaluate_saas_unit_economics",
    "arguments": {
    "prior_qtr_arr": 8000000.0,
    "current_qtr_arr": 9200000.0,
    "prior_qtr_sm_expense": 1100000.0,
    "gross_margin_pct": 78.0,
    "average_monthly_churn_pct": 0.65
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
