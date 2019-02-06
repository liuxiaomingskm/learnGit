users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]
def num_friends(user):
    num_of_friends=0
    id_no=None
    for dic in users:
        if dic['name']==user:
            id_no=dic["id"]
    for tup in friendship:
        if id_no in tup:
            num_of_friends+=1
    return num_of_friends

def sort_by_num_friends():
    result = []
    for usersName in users:
        a = num_friends(usersName)
        result.append({"num": a, "name" : usersName["name"]})

    result1 = sorted(result, key = lambda x:x["num"], reverse = True)
    print (result1)


def mean_num_friends(x):
    
    sum = 0
    for num in x:
        sum += num
    size = len(x)
    return sum / size 
    
    

def median_num_friends(x):
    
    x.sort()
    size = len(x)
    if size & 1 :
        return x[size / 2]
    else:
        return (x[size / 2 - 1] + x[size / 2]) / 2
       
    


num_friends1=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print("mean = {}".format(mean_num_friends(num_friends1)))

print("median = {}".format(median_num_friends(num_friends1)))

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

def demo1():
    mu, sigma = 0 , 1
    sampleNo = 100000
    np.random.seed(0)
    s = np.random.normal(mu,sigma,sampleNo)

    plt.hist(s,bins = 25, normed = True)
    plt.show()


def normal_pdf(x, mu=0, sigma=1):
    y_sig = np.exp(-(x - mu) ** 2 /(2* sigma**2))/(math.sqrt(2*math.pi)*sigma)
    return y_sig

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '-', label='mu=0,sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], '-', label='mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, sigma=-1) for x in xs], '-', label='mu=0,sigma=-1')
plt.legend()
plt.show()


      
      
