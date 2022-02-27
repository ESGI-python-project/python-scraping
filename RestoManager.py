

def addResto(title):
    import csv
    listResto = []
    with open("restos.csv", "r") as csv_file:
        theread = csv.reader(csv_file, delimiter=';')
        for r in theread:
            res = ""
            for c in r:
                res = res+c
            listResto.append(res)
    with open("restos.csv", "w") as csv_file:
        thewriter = csv.writer(csv_file, delimiter=';')
        for r in listResto:
            thewriter.writerow(r)
        thewriter.writerow(title)

def deleteResto(title):
    import json
    listResto = []
    listResto = json.loads("restos.json")
    res = []
    for restaurant in listResto["Restos"]:
        if lien["Titre"] != title:
            res.append(restaurant)
    with open("restos.json", "w") as json_file:
        json.dump({"Restos":res}, json_file)

def getRestos():
    import csv
    listResto = []
    with open("restos.csv", "r") as csv_file:
        theread = csv.reader(csv_file, delimiter=';')
        for r in theread:
            if r:
                res = ""
                for c in r:
                    res = res+c
                listResto.append(res)
    return listResto
