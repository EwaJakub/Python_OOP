import re

with open('text.txt', 'r') as fin:
    text_to_search = fin.read()
    print(re.findall(r"autor", text_to_search))
    print(re.findall(r"\d+%", text_to_search))
    print(re.findall(r"\w+\.", text_to_search))
    print(re.findall(r"polski", text_to_search, re.I))
