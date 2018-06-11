dna = 'AATCTGCAC'
reverso = ""
for i in dna:
    if (i == 'A'):
        reverso += 'T'
    elif (i == 'T'):
        reverso += 'A'
    elif (i == 'C'):
        reverso += 'G'
    else:
        reverso += 'C'



print(reverso)