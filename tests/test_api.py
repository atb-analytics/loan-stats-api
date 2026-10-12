from fastapi.testclient import TestClient

from loan_stats_api.api import app

client = TestClient(app)


def test_rate_endpoint():
    response = client.post(
        "/delinquency",
        json=[{"days_past_due": 0}, {"days_past_due": 45}],
    )
    assert response.status_code == 200

def test_bad_data_rejected():
    response = client.post(
        "/delinquency",
        json=[{"days_past_due": "abc"}],
    )
    assert response.status_code == 422
