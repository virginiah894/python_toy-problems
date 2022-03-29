import random
import urllib.request

url = "http://norvig.com/ngrams/sowpods.txt"
file_to = "download_file.txt"
urllib.request.urlretrieve(url, file_to)
with open('download_file.txt') as dtf:
    words = dtf.readlines()
    ranword = random.choice(words)
    print(ranword)