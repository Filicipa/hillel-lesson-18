import requests
url = ("https://baconipsum.com/api?type=meat-and-filler")
#response = requests.get(url)
#print(response.text)

for response in range(5):
    response = requests.get(url)
    print(response.text)

