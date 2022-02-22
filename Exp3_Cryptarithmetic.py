import itertools
def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s

def solve(equation):
    # split equation in left and right
    left, right = equation.lower().replace(' ', '').split('=')
    print(left,right)
    # split words in left part
    left = left.split('+')
    print(left)
    # create list of used letters
    letters = set(right)
    print(letters)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)
    print(letters)

    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            print(' + '.join(str(get_value(word, sol)) for word in left) + " = {} (mapping: {})".format(get_value(right, sol), sol))

if __name__ == '__main__':
    solve(input())
