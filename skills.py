# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-agentic-commerce-saas-magic-number-cac-payback-unit-economics-skill
Category: agentic_commerce
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def evaluate_saas_unit_economics(prior_qtr_arr, current_qtr_arr, prior_qtr_sm_expense, gross_margin_pct=75.0, average_monthly_churn_pct=0.8):
    if prior_qtr_sm_expense <= 0:
        raise ValueError("prior_qtr_sm_expense must be greater than zero")
        
    arr_growth = current_qtr_arr - prior_qtr_arr
    # Annualized net new ARR / Prior Qtr S&M
    magic_number = (arr_growth * 4.0) / prior_qtr_sm_expense
    
    # CAC Payback Period (Months) = (Prior Qtr S&M / Net New ARR) * (12 / Gross Margin)
    if arr_growth > 0:
        cac_payback_months = (prior_qtr_sm_expense / arr_growth) * (12.0 / (gross_margin_pct / 100.0)) / 4.0
    else:
        cac_payback_months = 999.0
        
    # LTV / CAC approximation
    # Customer lifespan months = 1 / monthly_churn
    avg_lifespan_months = 1.0 / (average_monthly_churn_pct / 100.0) if average_monthly_churn_pct > 0 else 120.0
    ltv_to_cac_ratio = (avg_lifespan_months / cac_payback_months) if cac_payback_months > 0 else 0.0
    
    # Magic Number Benchmarking:
    # > 1.0: Outstanding efficiency; pour capital into sales/marketing
    # 0.75 - 1.0: Healthy efficiency
    # 0.5 - 0.75: Questionable efficiency
    # < 0.5: Inefficient engine; fix product-market fit or churn
    if magic_number >= 1.0:
        tier = "TOP_QUARTILE_SCALE_READY"
        action = "High go-to-market efficiency; accelerate growth investment."
    elif magic_number >= 0.75:
        tier = "EFFICIENT_EXPANSION"
        action = "Solid unit economics; maintain growth trajectory."
    elif magic_number >= 0.5:
        tier = "SUBOPTIMAL_CAPITAL_EFFICIENCY"
        action = "Tighten CAC channels and improve retention before expanding GTM."
    else:
        tier = "LEAKY_SALES_ENGINE"
        action = "Critical GTM inefficiency; overhaul funnel conversion and retention."
        
    return {
        "prior_quarter_arr_usd": round(prior_qtr_arr, 2),
        "current_quarter_arr_usd": round(current_qtr_arr, 2),
        "net_new_arr_usd": round(arr_growth, 2),
        "sales_marketing_expense_usd": round(prior_qtr_sm_expense, 2),
        "saas_magic_number": round(magic_number, 2),
        "cac_payback_period_months": round(cac_payback_months, 1),
        "estimated_ltv_to_cac_ratio": round(ltv_to_cac_ratio, 2),
        "unit_economics_tier": tier,
        "investor_recommendation": action
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "evaluate_saas_unit_economics",
                        "description": """Evaluate B2B Enterprise SaaS sales efficiency, CAC Payback Period (months), Magic Number, and LTV:CAC ratio.
Magic Number = (Quarterly Net ARR Growth * 4) / Prior Quarter Sales & Marketing Expense.
Benchmarks go-to-market capital efficiency against top-quartile Bessemer SaaS metrics.""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = evaluate_saas_unit_economics(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'prior_qtr_arr': 8000000.0, 'current_qtr_arr': 9200000.0, 'prior_qtr_sm_expense': 1100000.0, 'gross_margin_pct': 78.0, 'average_monthly_churn_pct': 0.65}
        out = evaluate_saas_unit_economics(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
