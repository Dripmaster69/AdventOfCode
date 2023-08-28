import collections

def Advent2015part1():
    with open("2015day.txt", "r", encoding="utf8") as f:
        var = f.readline()

    d = collections.defaultdict(int)
    for c in var:
        d[c] += 1
    print(int(d["("]) - int(d[")"]))

def Advent2015part2():
    with open("2015day.txt", "r", encoding="utf8") as f:
        var = f.readline()

    d = collections.defaultdict(int)
    for c in var:
        d[c] += 1
        if int(d["("]) - int(d[")"]) == -1: print(int(d["("]) + int(d[")"]))
Advent2015part2()