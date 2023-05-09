import requests
import time
from bs4 import BeautifulSoup
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    header = {"user-agent": "Fake user-agent"}
    try:
        result = requests.get(url, headers=header, timeout=3)
        if result.status_code == 200:
            return result.text
        return None
    except (requests.HTTPError, requests.ReadTimeout):
        return None


# Requisito 2
def scrape_updates(html_content):
    result = []

    soup = BeautifulSoup(html_content, "html.parser")
    links = soup.find_all("a", {"class": "cs-overlay-link"})

    for link in links:
        result.append(link["href"])

    return result


# Requisito 3
def scrape_next_page_link(html_content):
    if len(html_content) < 1:
        return None

    soup = BeautifulSoup(html_content, "html.parser")
    link = soup.find("a", {"class": "next page-numbers"})["href"]

    if link is not None:
        return link

    return None


# Requisito 4
def scrape_news(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    link = soup.find("link", {"rel": "canonical"})["href"]
    title = soup.find("h1", {"class": "entry-title"}).text.strip()
    timestamp = soup.find("li", {"class": "meta-date"}).text
    author = soup.find("a", {"class": "url fn n"}).text
    time_read = soup.find("li", {"class": "meta-reading-time"}).text.split()[0]
    summary = soup.find("div", {"class": "entry-content"}).p.text.strip()
    category = soup.find("span", {"class": "label"}).text

    result = {
        "url": link,
        "title":  title,
        "timestamp": timestamp,
        "writer": author,
        "reading_time": int(time_read),
        "summary": summary,
        "category": category
    }

    return result


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    all_news = []
    while len(all_news) < amount:
        page = fetch(url)
        all_links = scrape_updates(page)
        for link in all_links:
            if len(all_news) < amount:
                new_page = fetch(link)
                news = scrape_news(new_page)
                all_news.append(news)
        next_page = scrape_next_page_link(page)
        url = next_page

    create_news(all_news)

    return all_news
