import numpy
import pandas

def findTotalDistance(filename):
    df = pandas.read_csv(filename, header=None, delimiter='   ')
    arr1 = df.iloc[:,0].to_numpy()
    arr2 = df.iloc[:,1].to_numpy()

    numpy.sort(arr1)
    numpy.sort(arr2)

    total = numpy.sum(numpy.absolute(numpy.subtract(arr1, arr2)))

    return abs(total)

if __name__ == '__main__':
    
    dist = findTotalDistance('realData')
    print(dist)
