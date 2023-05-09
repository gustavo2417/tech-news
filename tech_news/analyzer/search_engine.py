from tech_news.database import search_news


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
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
