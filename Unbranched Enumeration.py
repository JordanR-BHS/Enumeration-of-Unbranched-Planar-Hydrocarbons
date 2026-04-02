print("ENUMERATION OF TERMINALLY MONOSUBSTITUTED ACYCLIC PLANAR HYDROCARBONS")

partialPermutations = []

x = []
y = []
z = []

stereoCounting = 0
stereoIsomers = 0

bonds = []

numCarbons = int(input("How many carbon atoms? (must be even) "))

numExpansions = int(numCarbons / 2) - 1

for i in range(numExpansions + 1):
    partialPermutations.append([])

partialPermutations[0].append([1, "root", 3, "C"])
partialPermutations[0].append([1, "root", 2, "C"])

for i in range(numExpansions):
    for j in range(len(partialPermutations[i])):
        if partialPermutations[i][j][4 * i + 2] == 3:
            for k in range(len(partialPermutations[i][j])):
                x.append(partialPermutations[i][j][k])
                y.append(partialPermutations[i][j][k])
            x.append(1)
            x.append("C")
            x.append(3)
            x.append("C")
            y.append(1)
            y.append("C")
            y.append(2)
            y.append("C")
            partialPermutations[i + 1].append(x)
            partialPermutations[i + 1].append(y)
            x = []
            y = []
        elif partialPermutations[i][j][4 * i + 2] == 2:
            for k in range(len(partialPermutations[i][j])):
                x.append(partialPermutations[i][j][k])
                y.append(partialPermutations[i][j][k])
                z.append(partialPermutations[i][j][k])
            x.append(2)
            x.append("C")
            x.append(2)
            x.append("C")
            y.append(1)
            y.append("C")
            y.append(3)
            y.append("C")
            z.append(1)
            z.append("C")
            z.append(2)
            z.append("C")
            partialPermutations[i + 1].append(x)
            partialPermutations[i + 1].append(y)
            partialPermutations[i + 1].append(z)
            x = []
            y = []
            z = []

permutations = partialPermutations[-1]

for i in range(len(permutations)):
    for j in range(int(len(permutations[i]) / 2)):
        bonds.append(permutations[i][2 * j])
    for k in range(len(bonds) - 1):
        if bonds[k] == 2 and bonds[k + 1] == 1:
            stereoCounting += 1

    if stereoCounting != 0:
        stereoIsomers = 2 ** stereoCounting - 1

    for l in range(stereoIsomers):
        permutations.append(permutations[i])

    bonds = []
    stereoCounting = 0
    stereoIsomers = 0

piBonds = 0
piBondsCount = []
formulaCount = [1]
formulae = []

for i in range(len(permutations)):
    for j in range(int(len(permutations[i]) / 2)):
        bonds.append(permutations[i][2 * j])
    for k in range(len(bonds)):
        piBonds += (bonds[k] - 1)
    piBondsCount.append(piBonds)

    bonds = []
    piBonds = 0

piBondsCount.sort()
formulae.append(2 * numCarbons + 2 - 2 * piBondsCount[0] - 1)

for i in range(len(piBondsCount) - 1):
    if piBondsCount[i] == piBondsCount[i + 1]:
        formulaCount[len(formulaCount) - 1] += 1
    else:
        formulaCount.append(1)
        formulae.append(2 * numCarbons + 2 - 2 * piBondsCount[i + 1] - 1)

print(f"The total number of permutations for {numCarbons} carbon atoms is {len(permutations)}.")
for i in range(len(formulaCount)):
    if formulae[i] != 1:
        print(f"There is/are {formulaCount[i]} isomer(s) of formula C{numCarbons}H{formulae[i]}F.")
    else:
        print(f"There is/are {formulaCount[i]} isomer(s) of formula C{numCarbons}HF.")

