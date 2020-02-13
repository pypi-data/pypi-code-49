from itertools import groupby
from collections import defaultdict, namedtuple
from itertools import product
import nltk


def version_grid(xs, ys):
    '''Create a grid for longest common subsequence calculations.
    This includes not only letters but also sentences e.g. "아버지 가방에 들어가신다"

    Returns a grid where grid[(j, i)] is a pair (n, move) such that
    - n is the length of the LCS of prefixes xs[:i], ys[:j]
    - move is \, ^, <, or e, depending on whether the best move
      to (j, i) was diagonal, downwards, or rightwards, or None.

    Example:
       T  A  R  O  T
    A 0< 1\ 1< 1< 1<
    R 0< 1^ 2\ 2< 2<
    T 1\ 1< 2^ 2< 3\
    '''
    Cell = namedtuple('Cell', 'length move')
    grid = defaultdict(lambda: Cell(0, 'e'))
    sqs = product(enumerate(ys), enumerate(xs))
    for (j, y), (i, x) in sqs:

        # The case when lines are similar
        if is_similar(x, y):
            cell = Cell(grid[(j-1, i-1)].length + 1, '\\*')
        elif x == y:
            cell = Cell(grid[(j-1, i-1)].length + 1, '\\')
        else:
            left = grid[(j, i-1)].length
            over = grid[(j-1, i)].length
            if left < over:
                cell = Cell(over, '^')
            else:
                cell = Cell(left, '<')
        grid[(j, i)] = cell
    return grid


def complement_indices(A, B):
    '''Returns a complement(A-B) indices in A

       Returns the indices of A's the complementary set

       Example:
       A = ['a', 'b', 'c']
       B = ['b','c']
       result = complement_indices(A,B)
       print(result)
       # prints [0]

    '''
    indices = []
    for idx, i in enumerate(A, start=0):
        if i not in B:
            indices.append(idx)

    return indices


def version_diff(old, new):
    '''Return a longest common subsequence(lcs) of old, new, and updated lines within lcs'''
    # Create the LCS grid, then walk back from the bottom right corner
    grid = version_grid(old, new)
    i, j = len(old) - 1, len(new) - 1
    update_lcs_lines = []
    lcs = list()
    for move in iter(lambda: grid[(j, i)].move, 'e'):
        if move == '\\':
            lcs.append(old[i])
            i -= 1
            j -= 1
        elif move == '\\*':
            update_lcs_lines.append((i, j))
            i -= 1
            j -= 1
        elif move == '^':
            j -= 1
        elif move == '<':
            i -= 1

    lcs.reverse()
    return lcs, update_lcs_lines


def lists(lst):
    '''Returns lists of consecutive items in a list'''
    pos = (j - i for i, j in enumerate(lst))
    t = 0
    for _i, els in groupby(pos):
        l = len(list(els))
        el = lst[t]
        t += l
        yield list(range(el, el+l))


def is_similar(xs, ys):
    '''Returns when two strings are similar
    Similarity is achieved when:
    - the length of both strings are same
    - there is only one letter difference between them(i.e. Levenstein Distance between them is 1)

    Example
    is_similar("abcd", "abed") # returns true
    '''
    return len(xs) == len(ys) and nltk.edit_distance(xs, ys) == 1
