from loan_stats_api.metrics import delinquency_rate

def test_empty_list_returns_zero():
    assert delinquency_rate([]) == 0.0

def test_all_current():
    loans = [
        {"days_past_due": 0},
        {"days_past_due": 10},
        {"days_past_due": 29},
    ]
    assert delinquency_rate(loans) == 0.0

def test_mixed():
    loans = [
        {"days_past_due": 0},
        {"days_past_due": 5},
        {"days_past_due": 45},
        {"days_past_due": 60},
    ]
    assert delinquency_rate(loans) == 0.5
