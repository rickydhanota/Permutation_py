#Permutation
#write a function that takes in an array of unique integers and returns an array of all permuations of those integers in no particular order
#If the input array is empty, the function should return an empty array

#array = [1, 2, 3]
#sample output; [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 2, 1]]

def getPermutations(array):
    permutations = []
    permutationsHelper(0, array, permutations)
    return permutations

def permutationsHelper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i, j)
            permutationsHelper(i+1, array, permutations)
            swap(array, i, j)

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

print(getPermutations([1, 2, 3]))