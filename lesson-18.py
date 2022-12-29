import requests
import datetime
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

word = "pancetta"
amount_pancetta = 0
for elements in paragraphs:
    if word in elements.lower():
        amount_pancetta = amount_pancetta + 1

print(f"Number of paragraphs with pancetta: {amount_pancetta}")

date_now = datetime.datetime.now()
with open("lesson-18.txt", 'w', encoding='utf8') as f:
    f.write("Alexander " f'{date_now}\n' 
            f'{amount_pancetta}\n')
f.close()

with open("lesson-18.txt", 'a', encoding='utf8') as f:
    f.writelines(f'{elements}\n' for elements in paragraphs)
f.close()
