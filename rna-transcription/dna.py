def to_rna(dna):
    list1 = {
        'A': 'U',
        'G': 'C',
        'T': 'A',
        'C': 'G'
    }

    complement = ""

    for i in dna:
        if i in list1:
            complement += list1[i]
    return complement
