# TODO решите задачу

import json

FILENAME = "input.json"

def task():
    with open(FILENAME) as f:
        file_data = json.load(f)

    ...  # TODO отсортировать и вернуть список словарей

    score_i = [i["score"] for i in file_data]
    weight_i = [i["weight"] for i in file_data]

    pr = [i * j for i, j in zip(score_i, weight_i)]

    return sum(pr)





print(f"{task():.3f}")
