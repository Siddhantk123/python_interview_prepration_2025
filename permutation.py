def find_permutation(string):
    if len(string) == 1:
        return string

    def give_combination_as_per_seq(string):
        combination=[]
        for index, char in enumerate(string):
            current_char = char
            remaining_string = string[:index]+string[index+1:] #slicing
            combination.append(current_char+remaining_string)
        return combination

    permutation=[]
    for index, char in enumerate(string):
        current_char = char
        remaining_string = string[:index]+string[index+1:]
        permutation.extend(give_combination_as_per_seq(current_char+remaining_string)) #passing diff seq eg abc,bac,cab
    return list(set(permutation))

print(find_permutation(string="abc"))
    

    