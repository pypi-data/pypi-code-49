from .utils import *
from .formatters import Added, Removed, Updated
import nltk


def diff(old, new):
    '''
    Returns difference analysis between two texts ( remove | add | update) with 3 formatters ( Added | Removed | Updated )
    '''
    # Split texts with newline('\n')
    lines_new = new.split('\n')
    lines_old = old.split('\n')

    # Get LCS and lcs indices in their old/new text with updates
    lcs, update_lcs_lines = version_diff(
        lines_old, lines_new)

    # Get removed lines
    removed_lines = complement_indices(lines_old, lcs)

    # Get added lines
    added_lines = complement_indices(lines_new, lcs)

    # Get updated lines tuple get details
    updated_lines_old = [i[0] for i in update_lcs_lines]
    updated_lines_new = [i[1] for i in update_lcs_lines]
    updated_sentences = [(lines_old[i[0]], lines_new[i[1]])
                         for i in update_lcs_lines]

    # Remove updated line case in removed lines
    removed_lines = [x for x in removed_lines if x not in updated_lines_old]

    # Remove updated line case in added lines
    added_lines = [x for x in added_lines if x not in updated_lines_new]

    # Split removed lines part by part
    split_removed_lines = list(lists(removed_lines))

    split_removed_sentences = [[lines_old[j]
                                for j in i] for i in split_removed_lines]

    # Split added lines part by part
    split_added_lines = list(lists(added_lines))

    split_added_sentences = [[lines_new[j]
                              for j in i] for i in split_added_lines]

    return [Removed(split_removed_lines[i], split_removed_sentences[i]) for i in range(len(split_removed_lines))], [Added(split_added_lines[i], split_added_sentences[i]) for i in range(len(split_added_lines))], [Updated(update_lcs_lines[i], updated_sentences[i]) for i in range(len(updated_sentences))]
