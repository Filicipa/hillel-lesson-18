import requests
from datetime import datetime
import sys

def get_paragraphs_amount():
    p = 5
    try:
        p_input = input("Enter amount of paragraphs: ")
        if int(p_input) > 0:
            p = int(p_input)
    except:
        print("Something went wrong with paragraphs or it was 0")
        sys.exit()
    return p


paragraphs_count = get_paragraphs_amount()

url = f"https://baconipsum.com/api/?type=meat-and-filler&paras={paragraphs_count}&format=text"

response = requests.get(url)
text = response.text
paragraphs = text.split("\n\n")
print(paragraphs)

print("-----NOW REVERSE-----")
paragraphs.reverse()
for elements in paragraphs:
    print(elements)

amount_pancetta = sum(1 if "pancetta" in e.lower() else 0 for e in paragraphs)

print(f"Number of paragraphs with pancetta: {amount_pancetta}")

date_now = datetime.now()
with open("lesson-18.txt", 'w', encoding='utf8') as f:
    f.write("Alexander " f'{date_now}\n'
            f'{amount_pancetta}\n')
    f.writelines(f'{elements}\n' for elements in paragraphs)
f.close()
