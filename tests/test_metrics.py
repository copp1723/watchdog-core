from api.services.metrics import calc_lead_source_roi, calc_rep_leaderboard
from api.services.metrics_sales import cost_per_sale, cost_per_sale_by_vendor, sales_by_salesperson, new_vs_used
from tests.fixtures import df

def test_lead_source_roi():
    out = calc_lead_source_roi(df)
    # NeoIdentity net_profit: 4000-800=3200, AcmeCorp: 3200-1000=2200
    assert any(row['lead_source'] == 'NeoIdentity' and row['net_profit'] == 3200 for row in out)
    assert any(row['lead_source'] == 'AcmeCorp' and row['net_profit'] == 2200 for row in out)

def test_cost_per_sale():
    out = cost_per_sale(df)
    # (800+1000)/2 = 900
    assert out == 900

def test_rep_leaderboard():
    out = calc_rep_leaderboard(df)
    # Alice: 3200, Bob: 2200
    assert any(row['sales_rep_name'] == 'Alice' and row['net_profit'] == 3200 for row in out)
    assert any(row['sales_rep_name'] == 'Bob' and row['net_profit'] == 2200 for row in out)

def test_cost_per_sale_by_vendor_headline():
    out = cost_per_sale_by_vendor(df)
    keys = ['worst_vendor', 'worst_cps', 'best_vendor', 'best_cps', 'shift_pct']
    for k in keys:
        assert k in out['headline']

def test_sales_by_salesperson_headline():
    out = sales_by_salesperson(df)
    keys = ['top_rep', 'top_sales', 'low_rep', 'low_sales']
    for k in keys:
        assert k in out['headline']

def test_new_vs_used_headline():
    out = new_vs_used(df)
    keys = ['new_count', 'used_count']
    for k in keys:
        assert k in out['headline'] 