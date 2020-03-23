import os
d = set()

filename = "webster-dictionary.txt"

raw = open("webster-dictionary.txt", "r")

for w in raw:
    w2 = w.replace("-", "").replace(" ", "")
    if w2.strip().isalpha():
        d.add(w2.lower())

revised = open(filename[:-4]+"-revised.txt", "w")
raw.close()

for w in sorted(list(d)):
    if len(w) > 4: revised.write(w)

revised.close()