import os
import urllib.request
import time
os.system('color a')

def getStockName(ticker):
    url = f'https://google.com/search?q=NADAQ:+{ticker}'

    # Perform the request
    request = urllib.request.Request(url)

    # Set a normal User Agent header, otherwise Google will block the request.
    request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    raw_response = urllib.request.urlopen(request).read()

    # Read the repsonse as a utf-8 string
    html = raw_response.decode("utf-8")


    from bs4 import BeautifulSoup

    # The code to get the html contents here.

    soup = BeautifulSoup(html, 'html.parser')

    givs = soup.select("#search div.oPhL2e")
    for giv in givs:
        names = giv.select("span")
        if (len(names) >= 1):

            # Print the title
            company = names[0]
            print(company.get_text())

def getStockPrice(ticker):

    url = f'https://google.com/search?q=NADAQ:+{ticker}'

    # Perform the request
    request = urllib.request.Request(url)

    # Set a normal User Agent header, otherwise Google will block the request.
    request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    raw_response = urllib.request.urlopen(request).read()

    # Read the repsonse as a utf-8 string
    html = raw_response.decode("utf-8")


    from bs4 import BeautifulSoup

    # The code to get the html contents here.

    soup = BeautifulSoup(html, 'html.parser')

    # Find all the search result divs
    divs = soup.select("#search div.wGt0Bc")
    
    for div in divs:
        # Search for a h3 tag
        results = div.select("span")

        # Check if we have found a result
        if (len(results) >= 1):

            # Print the title
            span = results[0]
            return span.get_text()




if __name__ == '__main__':
    ticker = input('What is the ticker for the stock? ')
    getStockName(ticker)
    while True:
        print(getStockPrice(ticker))
        time.sleep(10)