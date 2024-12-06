import numpy
import pandas

def findTotalDistance(arr1, arr2):
    numpy.sort(arr1)
    numpy.sort(arr2)

    total = numpy.sum(numpy.subtract(arr1, arr2))

    return abs(total)

if __name__ == '__main__':
    df = pandas.read_csv('realData', header=None, delimiter='   ')
    arr1 = df.iloc[:,0].to_numpy()
    arr2 = df.iloc[:,1].to_numpy()
    
    dist = findTotalDistance(arr1, arr2)
    print(dist)
