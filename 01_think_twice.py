shift = 2
# english_alphabet =
# german_alphabet
#
# alphabet = german_alphabet

list_length = 26

# take index position and printing new index position based on amount needing to be shifted
for i in range(list_length):
    new_index = i + shift
    # if the new_index position is bigger than the list lenth, wraps to beging of index (e.g. y->a)
    if new_index > (list_length-1):
        new_index = new_index - list_length
    print(i, new_index)
