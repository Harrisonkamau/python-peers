import string


# your functions
def decode(cipher):
    list1 = dict(zip(string.ascii_lowercase, range(26)))
    list2 = dict(zip(range(25, -1, -1), string.ascii_lowercase))

    # print list2

    plain = ""

    for i in cipher.lower():
        if i.isalpha():
            plain += list2[(list1[i] + 26) % 26]
    return plain

# print decode("zyx")


def encode(plain):
    list1 = dict(zip(string.ascii_lowercase, range(26)))
    list2 = dict(zip(range(25, -1, -1), string.ascii_lowercase))

    cypher = ""

    for i in plain.lower():
        if i.isalpha():
            cypher += list2[list1[i]]
    return cypher

# print encode("abc")
