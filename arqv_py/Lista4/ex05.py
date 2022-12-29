def isanagrama(plv1: str, plv2: str):
    if len(plv1) != len(plv2):
        return False
    else:
        plv1 = list(plv1)
        plv2 = list(plv2)

        plv1.sort()
        plv2.sort()

        if plv1 == plv2:
            return True
        else:
            return False


plv1 = input('Digite uma palavra: ').upper().strip()
plv2 = input('Digite outra palavra: ').upper().strip()

if isanagrama(plv1, plv2) is True:
    print('É um anagrama.')
else:
    print('Não é um anagrama.')
