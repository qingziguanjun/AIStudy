#!/usr/bin/python
#!encoding:utf-8

from numpy import *
import operator

def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, lables, k):
    #一共有多少个点，点集的数量
    dataSetSize = dataSet.shape[0]
    #tile 是要构造出 dataSetSize个重复点，和dataSet数量一样，正好做个减法
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    #计算每个点相减后每个维度各自的平方
    sqDiffMat = diffMat ** 2
    #把各个维度的平方加在一起，就是欧氏距离
    sqDistances = sqDiffMat.sum(axis=1)
    #平方开根号
    distances = sqDistances**0.5
    #对这些距离排序，sortedDistIndicies是从小到大距离的点的序号
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        #只取距离近的前k个点，投票，哪个类别数量最多
        voteIlabel = lables[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
    #最后排序统计结果
    sortedClassCount = sorted(classCount.iteritems(),
                                  key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


group, labels = createDataSet()
classResult = classify0([0, 0], group, labels, 3)
print classResult

