import json

# dictfile = open("words_dictionary.json", "r")
# dictionary = [k.lower() for k in json.loads(dictfile.read()).keys()]

dictfile = open("webster-dictionary-revised.txt", "r")
dictionary = []

for d in dictfile:
    dictionary += [d.strip()]

domfile = open("tlds-alpha-by-domain.txt", "r")
domains = []
for d in domfile:
    domains += [d.strip().lower()]

endings = open("endings.txt", "w")
unrest = open("unrestricted.txt", "w")

ur, ed = set(), set()

for d in domains:
    for w in dictionary:
        i = w.find(d)
        delta = len(w) - i
        if i > 0:
            ur.add(w[:i]+"."+d+"\n")
            if delta == len(d):
                ed.add(w[:i]+"."+d+"\n")

for w in ur:
    unrest.write(w)

for w in ed:
    endings.write(w)




