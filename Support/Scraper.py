#ResumeBuilder
#Evangellos Wiegers
#April 17, 2020

#Note: make sure for macOS: Macintosh HD > Applications > Python3.7 -> "Install Certificates.command" is clocked

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bsoup
import traceback
import sys

def scrape(myURL):
    '''
    Function fo scrape a url of a job posting for any relevant keywords
    :param myURL: the string URL of the webpage of the  job posting
    :return: a list of string keywords scraped from the webpage of the url
    '''

    try:
        #Opening connection to page of url
        uClient = uReq(myURL)
        #Opening html file from connected url
        postingHtml = uClient.read()
        #Closing connection to page
        uClient.close()

        #Parsing the html
        postingSoup = bsoup(postingHtml, "html.parser")
        # print(postingSoup.prettify())

        #Getting string of all text of page
        keywords = postingSoup.get_text()

        #Removing useless characters and words froms string
        rep = [",", "/", "-", ":", ".", "|", "\n"]
        for i in rep:
            keywords = keywords.replace(i, " ")
        #Recreating list of keywords
        keywords = [t for t in keywords.casefold().split(" ") if t]
        blacklist = ["the", "at", "with", "and", "they", "their", "of", "in", "to", "that", "are", "on",
                        "from", "can", "get", "our", "your", "or", "you", "have", "is", "for", "well", "while", "own", "them",
                        "done", "will", "able", "others", "will", "a", "as", "we", "www", "com"]
        keywords = [t for t in keywords if t not in blacklist]
    except IOError as err:
        print("I/O Error: {0}".format(err))
    except ValueError as err: 
        print("Value Error: {0}".format(err))
    except:
        print("Unexpected Error:", sys.exc_info()[0])
    finally:
        #Returning list of keywords
        return keywords if not None else []


#Main testing
if __name__ == '__main__':
    #Getting url from user
    myURL = input("Enter the URL of the job posting: ")
    try:
        print(scrape(myURL))
    except Exception as err:
        print(err)
