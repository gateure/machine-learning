import numpy
def sig(x):
    return 1/(1+numpy.exp(-x))

inputs = [0, 1]
answer = 0
weights = [-2,-2]
bias = 0.1
totalcost = 0

for k in range(1000):
    activation = 0
    outputs = 0
    for i in range(len(weights)):
        outputs += (weights[i]*inputs[i])+bias
    activation = sig(outputs)
    totalcost += (activation-answer)**2
    cost = totalcost/(k+1)
    for i in range(len(weights)):
        weights[i] -= 0.1*(inputs[i])*(sig(outputs)*(1-sig(outputs)))*(2*(activation-answer))
        bias -= 0.1*(sig(outputs)*(1-sig(outputs)))*(2*(activation-answer))#(cost/activation)
    print(activation)


