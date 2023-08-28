def Advent2015part1():
    with open("2015day2.txt", "r", encoding="utf8") as f:
        list = f.readlines()
        tot_paper_sum = 0
        for x in list:
            splitx = x.split("x")
            
            tot_paper_sum = tot_paper_sum + (2*int(splitx[0])*int(splitx[1]) + 2*int(splitx[1])*int(splitx[2]) + 2*int(splitx[0])*int(splitx[2]))
            slack = min(int(splitx[0])*int(splitx[1]), int(splitx[1])*int(splitx[2]), int(splitx[0])*int(splitx[2]))
            tot_paper_sum += slack
        print(tot_paper_sum)
Advent2015part1()

def day2_1():
    total = 0
    for line in open('2015day2.txt'):
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        area = 2*l*w + 2*w*h + 2*h*l
        slack = min(l*w, w*h, h*l)
        total += area + slack
    print(total)
#day2_1()