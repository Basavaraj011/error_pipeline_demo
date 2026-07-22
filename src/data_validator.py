from utils import log_message


def validate_data(data):


    valid = [] 

    for record in data:

        if not is_valid_id(record):
            continue

        if not is_valid_name(record):
            continue

        if not is_valid_score(record):
            continue

        # Ensure score and bonus are integers
        if 'score' in record:
            try:
                record['score'] = int(record['score'])
            except (ValueError, TypeError):
                continue
        if 'bonus' in record:
            try:
                record['bonus'] = int(record['bonus'])
            except (ValueError, TypeError):
                continue

        valid.append(record)

    return valid


def is_valid_id(record):

    if record["id"] < 0:
        return False

    return True


def is_valid_name(record):

    name = record["name"]

    if not name:
        return False

    if len(name) < 3:
        return False

    return True


def is_valid_score(record):

    score = record["score"]

    if score < 0:
        return False

    if score > 100:
        return False

    return True