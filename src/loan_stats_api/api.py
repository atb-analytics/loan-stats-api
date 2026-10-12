from fastapi import FastAPI 
from pydantic import BaseModel

from loan_stats_api.metrics import delinquency_rate

app = FastAPI()

class Loan(BaseModel):
    days_past_due: int

@app.post("/delinquency")
def get_rate(loans: list[Loan]) -> float:
    return delinquency_rate([loan.model_dump() for loan in loans])
