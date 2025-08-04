def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    pass
    #print(L)
    #print(len(L))
    
    if len(L)>2:
        return L[1]
    else:
        return None
    

    #def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.     
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    pass

    racers[0],racers[-1] = racers[-1],racers[0]

a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

print((a[1]), a[2])

 
arrivals = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
name = "Mona"

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    pass

    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1

resultados = fashionably_late(arrivals, name)

print(resultados)

num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

# TODO: Fill in values for the variables below
avg_first_seven = sum(num_customers[:7])/7
avg_last_seven = sum(num_customers[-7:])/7 
max_month = max(num_customers)
min_month = min(num_customers)
#print(num_customers[-7:])
#print(avg_last_seven)
#print(max_month)
#print(min_month)

def percentage_liked(ratings):
    
    list_liked = [i>=4 for i in ratings]
    #print(list_liked)
    # TODO: Complete the function
    percentage_liked = sum(eva == True for eva in list_liked)/len(ratings)
    
    return percentage_liked
    

# Do not change: should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])



