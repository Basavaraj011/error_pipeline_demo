import datetime


# Fixed bug: bonus_factor should be a float
bonus_factor = 1.5


def log_message(msg):

    time = datetime.datetime.now().strftime("%H:%M:%S")

    print(f"[{time}] {msg}")


def calculate_bonus(score):

    # BUG: multiplying int by string
    # e.g. 50 * "1.5" -> "1.51.51.5..." (string)
    bonus = score * bonus_factor
    print("Bonus:", bonus)
    return bonus


def safe_divide(a, b):

    if b == 0:
        return 0

    return a / b


def format_name(name):

    return name.strip().title()


def debug_print(obj):

    print("DEBUG:", obj)


def calculate_average(values):

    if not values:
        return 0

    total = 0

    for v in values:
        total += v

    return total / len(values)