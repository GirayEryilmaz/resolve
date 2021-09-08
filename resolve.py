import random
from itertools import islice, product
def dist(word, other):
    """Return distance between words"""
    return sum(l1!=l2 for l1, l2 in zip(word, other))

def gen():
    """Generator for 6 letter words with the alphabet {A, C, G, T},
    but starts from a random position between 1 and 100 (not AAAAAAA).
    """
    r = random.randint(1,100)
    yield from islice(product('AGCT', repeat=6), r, None, 1)

def ok(candidate, already_picked):
    """Return True if candidate word is at least 3 distance away from all already accepted words"""
    for member in already_picked:
        if dist(member, candidate) < 3:
            return False
    return True

def find_words():
    def attempt():
        picked = set()
        new = gen()
        while True:
            try:
                candidate = ''.join(next(new))
            except StopIteration:
                break
            if ok(candidate, picked):
                picked.add(candidate)
        return sorted(picked)
    curr_res = attempt()
    while len(curr_res) < 96:
        curr_res = attempt()
    return random.sample(curr_res, 96)

def print_distance_matrix(words, output_path='output.txt'):
    """Output the given words with the distance matrix to a txt file"""
    with open(output_path, 'w') as o:
        print((' '*12), end='', file=o)
        print((' '*6).join(words), file=o)
        for word in words:
            print(word, end=' '*8, file=o)
            print(*(dist(word, other) if word!=other else '-' for other in words), sep=' '*11, file=o)

if __name__ == "__main__":

    words = find_words()
    words.sort()
    print_distance_matrix(words)
    print('Done.')
