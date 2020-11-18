import glob

# GBFS H1 2x4
search2x4 = glob.glob('2x4/*_gbfs-h1_2x4_search.txt')
solution2x4 = glob.glob('2x4/*_gbfs-h1_2x4_solution.txt')

lines = 0
success = 0
for i in solution2x4:
    f = open(i, "r")
    if f.readline() == ("No solution"):
        pass
    else:   
        num_lines = sum(1 for line in open(i))
        lines = lines + num_lines
        success +=1
        
print(lines)
print(lines/success)
print(success)


cost = 0
timeA = 0.0
yeet = 0
for i in solution2x4:
    f = open(i, "r")
    if f.readline() == ("No solution"):
        pass
    else:
        for last_line in f:
            pass
        last_line = last_line.split()
        cost = cost + int(last_line[0])
        timeA = timeA + float(last_line[1])
        yeet += 1 

print(cost)
print(cost/yeet)
print(timeA)
print(timeA/yeet)
print(yeet)