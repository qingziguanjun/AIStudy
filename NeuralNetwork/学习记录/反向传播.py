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



def network(input,weight1,weight2,weight3,out):
    result1 = forward(input, weight1)
    print(round(result1, 3))

    result2 = forward(input, weight2)
    print(round(result2, 3))
    out.append(round(result1, 3))
    out.append(round(result2, 3))
    result=[result1,result2]
    result3= forward(result,weight3)
    return round(result3, 3)
input=[0.35,0.9]
weight1=[0.1,0.8]
weight2=[0.4,0.6]
weight3=[0.3,0.9]
#输出层的结果
out=[]
target=0.5
for i in range(0,10):
    out = []
    result = network(input,weight1,weight2,weight3,out)
    print(result)
    #输出错误
    error=(target-result)*(1-result)*result
    error= round(error,4)
    print(error)

    #更新最近的输出层权重
    weight3[0]=round(weight3[0]+error*out[0],6)
    print(weight3[0])

    weight3[1]=round(weight3[1]+error*out[1],5)
    print(weight3[1])


    #更新隐藏层的权重
    eh1=error*weight3[0]*(1-out[0])*(out[0])
    print(eh1)
    eh2=error*weight3[1]*(1-out[1])*(out[1])
    print(eh2)

    weight1[0]=weight1[0] + eh1*input[0]
    print(weight1[0])

    weight1[1]=weight1[1] + eh2*input[0]
    print(weight1[1])

    weight2[0]=weight2[0] + eh1*input[1]
    print(weight2[0])

    weight2[1]=weight2[1] + eh2*input[1]
    print(weight2[1])



