import time
from bs4 import BeautifulSoup
import requests

def main():
    # URL of the web page you want to scrape
    url = 'https://youtubetranscript.com/?v=u4wV0-31oI0/'

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Wait for the page to load (you can adjust the time as needed)
    time.sleep(5)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all text nodes in the parsed HTML
    text_content = soup.find_all(text=True)

    # Extract and print the text content
    all_text = " ".join(text.strip() for text in text_content if text.strip())
    print("All Text Content:")
    print(all_text)

if __name__ == "__main__":
    main()

# import grequests
# from bs4 import BeautifulSoup
# import time

# def get_urls():
#     urls = []
#     for x in range(1,51):
#         urls.append(f'http://books.toscrape.com/catalogue/page-{x}.html')
#     return urls

# def get_data(urls):
#     reqs = [grequests.get(link) for link in urls]
#     resp = grequests.map(reqs)
#     return resp


# def parse_data(resp):
#     for r in resp:
#         sp = BeautifulSoup(r.text, 'lxml')
#         data = sp.find_all('article', {'class': 'product_pod'})
#         for item in data:
#             name = item.find('h3').text
#             price = item.find('p', {'class': 'price_color'}).text
#             print(name, price)
#     return

# if __name__ == '__main__':
#     start = time.perf_counter()
#     print("ok 1")
#     urls = get_urls()
#     print("ok 2")
#     resp = get_data(urls)
#     print("ok 3")
#     parse_data(resp)
#     print("ok 4")
#     fin = time.perf_counter() - start
#     print(fin)