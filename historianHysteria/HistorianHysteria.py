import numpy
import pandas

class HistorianHysteria:

    def findTotalDistance(arr1, arr2):
        numpy.sort(arr1)
        numpy.sort(arr2)
        
        total = numpy.sum(np.subtract(arr1, arr2))

        return abs(total)

    if __name__ == '__main__':
        df = pd.read_csv('realData', header=None, delimiter='\t')
        self.arr1 = df[[0]].to_numpy()
        self.arr2 = df[[1]].to_numpy()
        
        dist = findTotalDistance(arr1, arr2)
        print(dist)
