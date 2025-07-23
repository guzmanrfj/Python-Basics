def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    pass

    return(round(num,ndigits=2))

print(round_to_two_places(51.456789))


def to_smash(total_candies,friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % friends


print(to_smash(145,70))


def is_odd(n):
    return (n % 2) == 1

print("Is 350 odd?", is_odd(350))
print("Is 125 odd?", is_odd(125))

def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35) 

print(can_run_for_president(True, 19))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))
print(can_run_for_president(39,True))

def sign(num):
    
    if num > 0:
        return(1)
    elif num < 0:
        return(-1)
    else:
        return(0)

print(sign(0.000001))

def concise_is_negative(number):
    pass 
    return True if number < 0 else False

print(concise_is_negative(-8))

def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    pass

    return ketchup and mustard and onion


def wants_plain_hotdog(ketchup, mustard, onion):
    """Return whether the customer wants a plain hot dog with no toppings.
    """
    pass

    return not ketchup and not mustard and not onion

# One solution looks like:

#return not ketchup and not mustard and not onion
#We can also "factor out" the nots to get:

#return not (ketchup or mustard or onion)


def exactly_one_topping(ketchup, mustard, onion):
    """Return whether the customer wants exactly one of the three available toppings
    on their hot dog.
    """
    pass
    return (int(ketchup) + int(mustard) + int(onion)) == 1

#This condition would be pretty complicated to express using just and, or and not, but using boolean-to-integer conversion gives us this short solution:

#return (int(ketchup) + int(mustard) + int(onion)) == 1
#Fun fact: we don't technically need to call int on the arguments. Just by doing addition with booleans, Python implicitly does the integer conversion. So we could also write...

#return (ketchup + mustard + onion) == 1