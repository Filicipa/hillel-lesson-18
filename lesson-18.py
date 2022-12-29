import requests
url = "https://baconipsum.com/api?type=meat-and-filler"

paragraphs = list()

for x in range(5):
    response = requests.get(url)
    paragraphs.append(response.text)

for elements in paragraphs:
    print(elements)

print("-----NOW REVERSE-----")

paragraphs.reverse()
for elements in paragraphs:
    print(elements)

amount_pancetta = 0
for count_pancetta in paragraphs:
    if "pancetta" in elements:
        amount_pancetta = amount_pancetta + 1

print(f"Number of paragraphs with Pancetta: {amount_pancetta}")
