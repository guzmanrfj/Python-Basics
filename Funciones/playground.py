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

def can_run_for_president(age, is_natural_born_citizen, altura):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    return is_natural_born_citizen and (age >= 35) and (altura >= 1.85)

print(can_run_for_president(True, 19, 1.22))
print(can_run_for_president(1.67, 55, False))
print(can_run_for_president(55, 1.90, True))
print(can_run_for_president(True, 39, 1.92))

