aray={
    "indigo": 350,
    "blau": 450,
    "cian": 490,
    "verd": 550,
    "groc": 620,
    "taronja": 680,
    "vermell": 800,
}


array = ["indigo", "groc", "verd", "vermell", "blau", "cian", "taronja"]


for i in range(len(array)):
    for j in range(len(array) - i - 1):

        if aray [array[j]] > aray[array[j + 1]]:

            array[j], array[j + 1] = array[j + 1], array[j]

print(array)