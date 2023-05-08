import requests
import time
from bs4 import BeautifulSoup


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
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
