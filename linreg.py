# Written by Muaaz Abed, 1/5/2024

from statistics import mean

def main():
    print("Enter name of data file:")
    x, y = fileread(input())
    m, b, rsq = linreg(x, y)
    printresults(m, b, rsq)
    
# Reads file and processes data into lists
def fileread(filename):
    with open(filename, 'r') as file:
        input = file.read().split('\n')
        x = []
        y = []
        for i in input:
            pair = i.strip("()").split(",")
            x.append(int(pair[0]))
            y.append(int(pair[1]))
    return x, y
    
# Performs linear regression on data and returns results
def linreg(x, y):
    size = len(x)
    xavg = mean(x)
    yavg = mean(y)
    xyavg = mean([x[i] * y[i] for i in range(0, size)])
    m = ((xavg * yavg) - xyavg) / ((xavg ** 2) - (mean([i ** 2 for i in x])))
    b = yavg - m * xavg
    stderr, meanerr = 0, 0
    for i in range(0, size):
        stderr += (y[i] - (m * x[i] + b)) ** 2
        meanerr += (y[i] - yavg) ** 2
    rsq = 1 - (stderr / meanerr)
    return m, b, rsq

# Formats and prints regression results
def printresults(m, b, rsq):
    print("\nEquation: y = {0:0.2f}x".format(m), end = "")
    if round(b, 2) == 0:
        print(", r² = {0:0.2f}".format(rsq))
    elif b < 0:
        print(" - {0:0.2f}, r² = {1:0.2f}".format(b*-1, rsq))
    else:
        print(" + {0:0.2f}, r² = {1:0.2f}".format(b, rsq))
    
if __name__ == "__main__":
    main()