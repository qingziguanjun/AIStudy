import math


def sigmoid(input):
    return 1/(1+math.exp(-input))

def calcute(input,weight):
    size=len(input)
    out=0
    for i in range(0,size):
        out += input[i]*weight[i]
    #print(round(out,3))
    return out

def forward(input, weight):
    out = calcute(input, weight)
    result = sigmoid(out)
    return result



def network(input,weight1,weight2,weight3):
    result1 = forward(input, weight1)
    print(round(result1, 3))

    result2 = forward(input, weight2)
    print(round(result2, 3))

    result=[result1,result2]

    result3= forward(result,weight3)
    print(round(result3, 3))
input=[0.2,0.4]
weight1=[0.5,0.8]
weight2=[0.1,0.9]
weight3=[0.5,0.7]
network(input,weight1,weight2,weight3)

