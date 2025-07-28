c = 'it\'s ok'
print(len(c))


def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    pass
    if zip_code.isnumeric():
        return True
    else:
        return False
    


print(is_valid_zip("12345"))


frutas = [',manzana,', ',banana.', ',kiwi,']
def buscapalabra(lista,keyword):
    
    indices =[]
    for i, fruta in enumerate(frutas):
        #print(f"{i}: {fruta}")
        tokens = fruta.split()
        #print(tokens)
        normalized = [token.strip('.,').lower() for token in tokens]
        #print(normalized)

        if keyword.lower() in normalized:
            indices.append(i)
    return indices

print(buscapalabra(frutas,"MANZANA"))


