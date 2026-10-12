def delinquency_rate(loans: list[dict]) -> float:
    if len(loans) == 0:
        return 0.0
    late = 0
    for loan in loans:
        if loan["days_past_due"] >= 30:
            late = late + 1
    return late / len(loans)
