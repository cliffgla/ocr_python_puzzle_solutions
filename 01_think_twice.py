shift = 2
english_alphabet = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

coded_message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

decoded = " "
code = {}
# german_alphabet
#
alphabet = english_alphabet

list_length = len(alphabet)

# take index position and printing new index position based on amount needing to be shifted
for i in range(list_length):
    new_index = i + shift
    # if the new_index position is bigger than the list lenth, wraps to beging of index (e.g. y->a)
    if new_index > (list_length-1):
        new_index = new_index - list_length
    #print(alphabet[i], "-->", alphabet[new_index])
    # add new key-value pair to code dictionary
    code[alphabet[i]] = alphabet[new_index]

#print(code)

for letter in coded_message:
    if letter in alphabet:
        decoded += (code[letter])
    else:
        decoded += letter
print(decoded)
