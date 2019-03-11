# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]
    else:
        return [(word[:pos] + sequence[0] + word[pos:]) for word in get_permutations(sequence[1:]) for pos in range(len(word) + 1)]

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    inputs = ["abc", "ab", "c"]
    
    print("Input:", inputs[0])
    print("Expected Output:", ['abc', 'bac', 'bca', 'acb', 'cab', 'cba'])
    print("Actual Output:", get_permutations(inputs[0]))
    
    print("Input:", inputs[1])
    print("Expected Output:", ["ab", "ba"])
    print("Actual Output:", get_permutations(inputs[1]))
    
    print("Input:", inputs[2])
    print("Expected Output:", ["c"])
    print("Actual Output:", get_permutations(inputs[2]))
    

