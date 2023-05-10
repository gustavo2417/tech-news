from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    result = []
    news = find_news()
    ondened_categories = [category["category"] for category in news]
    returned = sorted(ondened_categories)
    counter = {}

    for i in returned:
        if i not in counter:
            counter[i] = 1
        counter[i] += 1

    while len(counter) > 0:
        new_category = max(counter, key=counter.get)
        counter.pop(new_category)
        if len(result) < 5:
            result.append(new_category)

    return result
