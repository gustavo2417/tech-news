from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    result = []
    new = search_news({"title": {"$regex": title, "$options": "i"}})
    for i in new:
        format_new = (i["title"], i["url"])
        result.append(format_new)

    return result


# Requisito 8
def search_by_date(date):
    result = []
    try:
        format_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        new = search_news({"timestamp": format_date})
        for i in new:
            format_new = (i["title"], i["url"])
            result.append(format_new)

        return result

    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    result = []
    new = search_news({"category": {"$regex": category, "$options": "i"}})
    for i in new:
        format_new = (i["title"], i["url"])
        result.append(format_new)

    return result
