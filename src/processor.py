from utils import log_message, calculate_bonus


def process_data(data):
    results = []
    for record in data:
        result = compute_result(record)
        results.append(result)
    return results

    return results

    score = record["score"]
    bonus = calculate_bonus(score)
    # Ensure bonus is numeric
    try:
        bonus = float(bonus)
    except (ValueError, TypeError):
        bonus = 0
    final_score = score + bonus
    return {
        "id": record["id"],
        "name": record["name"],
        "score": final_score
    }
        "name": record["name"],
        "score": final_score
    }
    total = 0
    for r in results:
        total += r["score"]
    if len(results) == 0:
        return 0
    return total / len(results)
    if len(results) == 0:
        return 0

    print("Processed Results")
    for r in results:
        print(
            r["id"],
            r["name"],
            r["score"]
        )        print(
            r["id"],
            r["name"],
            r["score"]
        )
