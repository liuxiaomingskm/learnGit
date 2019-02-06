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
    # TODO
    pass

def median_num_friends(x):
    # TODO
    pass



num_friends1=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]

print("mean={}".format(mean_num_friends(num_friends)))
print ("asdfb")