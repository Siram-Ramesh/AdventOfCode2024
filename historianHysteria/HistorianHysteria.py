import numpy
import pandas

def findTotalDistance(filename):
    df = pandas.read_csv(filename, header=None, delimiter='   ', engine='python')
    arr1 = df.iloc[:,0].to_numpy()
    arr2 = df.iloc[:,1].to_numpy()

    # print(arr1[:5])

    arr1 = numpy.sort(arr1)
    arr2 = numpy.sort(arr2)

    # print(arr1[:5])

    total = numpy.sum(numpy.absolute(numpy.subtract(arr1, arr2)))

    return abs(total)

def findSimilarity(filename):
    df = pandas.read_csv(filename, header=None, delimiter='   ', engine='python')
    map1 = {}
    map2 = {}

    for index, row in df.iterrows():
        if row[0] not in map1:
            map1[row[0]] = 1
        else:
            map1[row[0]] += 1
        if row[1] not in map2:
            map2[row[1]] = 1
        else:
            map2[row[1]] += 1

    total1 = 0
    total2 = 0
    for index, row in df.iterrows():
        if row[1] in map1:
            total1 += row[1]*map1[row[1]]
        if row[0] in map2:
            total2 += row[0]*map2[row[0]]

    if total1 != total2:
        raise Exception('The similarity scores of the 2 arrays are different!')

    return total1


if __name__ == '__main__':
    
    dist = findTotalDistance('realData')
    print(dist)
