result = []
def permute(data, i, length):
    if i == length:
        result.append(''.join(data))
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i + 1, length)
            data[i], data[j] = data[j], data[i]
            
ini_str = input('Give a string whose permutations you want to print:\n')
permute(list(ini_str), 0, len(ini_str))
result.sort()
# Printing result
print('Permutations of the string '+ini_str+' are:', end=' ')
print(result)
