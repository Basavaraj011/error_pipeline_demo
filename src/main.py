import traceback

from data_loader import load_data
from data_validator import validate_data
from processor import process_data
from utils import log_message
    results = []
    for record in data:
        result = compute_result(record)
        results.append(result)
    return results
    valid_data = validate_data(data)
def compute_result(record):
    score = record["score"]
    bonus = calculate_bonus(score)
    # Ensure bonus is numeric
    try:
        bonus = float(bonus)
    except (ValueError, TypeError):
        bonus = 0.0
    final_score = float(score) + bonus
    return {
        "id": record["id"],
        "name": record["name"],
        "score": final_score
    }

    total = 0
    for r in results:
        total += r["score"]
    if len(results) == 0:
        return 0
    return total / len(results)
if __name__ == "__main__":
    print("Processed Results")
    for r in results:
        print(r["id"], r["name"], r["score"])