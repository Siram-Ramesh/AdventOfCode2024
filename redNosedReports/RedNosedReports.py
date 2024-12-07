import csv

def countValidReports(filename):
    total = 0
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter = ' ')
        for row in reader:
            if isReportValid(row):
                total += 1
    return total


def isReportValid(row) -> bool:
    if len(row) > 1:
        incFlag = int(row[0]) < int(row[1])
    for idx, ele in enumerate(row):
        if idx == 0:
            continue
        prev = int(row[idx-1])
        curr = int(row[idx])
        if (abs(curr-prev) < 1 or 
                abs(curr-prev) > 3): 
            return False
        if incFlag and prev > curr:
            return False
        if (not incFlag) and prev < curr:
            return False
    return True

