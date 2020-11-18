import glob

# A STAR H1
aSearchH1 = glob.glob('txt/*_astar-h1_search.txt')
aSolutionH1 = glob.glob('txt/*_astar-h1_solution.txt')

# ASTAR H2
aSearchH2 = glob.glob('txt/*_astar-h2_search.txt')
aSolutionH2 = glob.glob('txt/*_astar-h2_solution.txt')

# GBFS H1
gbfsSearchH1 = glob.glob('txt/*_gbfs-h1_search.txt')
gbfsSolutionH1 = glob.glob('txt/*_gbfs-h1_solution.txt')

# GBFS H2
gbfsSearchH2 = glob.glob('txt/*_gbfs-h2_search.txt')
gbfsSolutionH2 = glob.glob('txt/*_gbfs-h2_solution.txt')

#UCS
ucsSolution = glob.glob('txt/*_ucs_solution.txt')
ucsSearch = glob.glob('txt/*_ucs_search.txt')


lines = 0
success = 0
#put input file here
for i in ucsSolution:
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
for i in ucsSolution:
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