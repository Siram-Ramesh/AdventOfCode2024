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

if __name__ == '__main__':
    
    dist = findTotalDistance('realData')
    print(dist)
