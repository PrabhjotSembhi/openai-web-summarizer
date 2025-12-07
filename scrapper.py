from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def get_website_content(url):
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.title.string if soup.title else "No title Found"
    if soup.body:
        for irrelevat in soup.body(["script", "style", "img", "input"]):
            irrelevat.decompose()
        text = soup.body.getText(separator="\n", strip=True)
    else:
        text = ""
    return (title + "\n\n" + text)[:2_000]




def get_website_links(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    return [link for link in links if link]


get_website_content("https://prabhjotsingh.in/")
print("urls\n")
print("urls\n")
print("urls\n")
print("urls\n")
print("urls\n")
get_website_links("https://prabhjotsingh.in/")