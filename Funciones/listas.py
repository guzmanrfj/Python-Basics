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