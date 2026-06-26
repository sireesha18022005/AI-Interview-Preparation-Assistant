def evaluate(answer):

    if len(answer) > 30:
        return 10, "Good Answer"

    elif len(answer) > 10:
        return 5, "Average Answer"

    else:
        return 2, "Need Improvement"