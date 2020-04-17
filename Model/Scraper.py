#make sure for macOS: Macintosh HD > Applications > Python3.7 -> "Install Certificates.command" is clocked

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bsoup

def scrape(myURL):
    #opening connection to page of url
    uClient = uReq(myURL)
    #opening html file from connected url
    postingHtml = uClient.read()
    #closing connection to page
    uClient.close()

    #parsing the html
    postingSoup = bsoup(postingHtml, "html.parser")
    #print(postingSoup.prettify())

    #getting string of all text of page
    keywords = " ".join([t.text for t in postingSoup.find_all("p") if t])

    #removing useless characters and words froms string
    rep = [",", "/", "-", ":", ".", "|"]
    for i in rep:
        keywords = keywords.replace(i, " ")
    #recreating list of keywords
    keywords = [t for t in keywords.casefold().split(" ") if t]
    blacklist = ["the", "at", "with", "and", "they", "their", "of", "in", "to", "that", "are", "on",
                     "from", "can", "get", "our", "your", "or", "you", "have", "is", "for", "well", "while", "own", "them",
                     "done", "will", "able", "others", "will", "a", "as", "we", "www", "com"]
    keywords = [t for t in keywords if t not in blacklist]

    #returning list of keywords
    return keywords


#main testing
if __name__ == "__main__":
    #getting url from user
    myURL = input("Enter the URL of the job posting: ")
    print(scrape(myURL))

