from  milibrerias.cuentasepara import cuenta_separa

def unir2strings(text1, text2):
    texto_unido = text1 + " " + text2
    lista, cantidad = cuenta_separa(texto_unido)
    print(texto_unido)
    print(lista)
    print(cantidad)

    return texto_unido, lista, cantidad


text1 = "kdcacadkc aDCMPadmcpADM PADCMPadmcp dcdc dcdc dcdca"
text2 = "pepfpefpef vbnfr tisoss dvdv ss dv bvfvfv gbfbf rvwv vvrwv dvvr rrvrv qqeq wrvwrv"

unir2strings(text1, text2)