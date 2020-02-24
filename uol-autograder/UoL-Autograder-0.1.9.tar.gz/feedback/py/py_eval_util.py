from inspect import getmembers, isfunction, signature, getfile, currentframe
import os, time, signal
import importlib
import json
from pathlib import Path
import subprocess
import numpy as np

PASS = "pass"
FAIL = "fail"
EXCEPTION = "exceptions"
EXCEPTION_TAG = "EXCEPTION:"
DURATION_SAMPLE_COUNT = 1000

def get_eval_util_path():
    return os.path.abspath(getfile(currentframe()))

class Lookup:
    eval_feedback = os.path.join(
        Path(get_eval_util_path()).parent.parent,
        "lookup/py_eval_feedback.json")

def get_module_functions(module):
    # Get every function in a module
    return [f[1] for f in getmembers(module) if isfunction(f[1])]

def levenshtein_ratio_and_distance(s, t, ratio_calc = False):
    """
    Source: https://www.datacamp.com/community/tutorials/fuzzy-string-python
    More on lev_distance: https://en.wikipedia.org/wiki/Levenshtein_distance

        levenshtein_ratio_and_distance:
        Calculates levenshtein distance between two strings.
        If ratio_calc = True, the function computes the
        levenshtein distance ratio of similarity between two strings
        For all i and j, distance[i,j] will contain the Levenshtein
        distance between the first i characters of s and the
        first j characters of t
    """
    # Initialize matrix of zeros
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)
    col, row = 0, 0
    
    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k

    # Iterate over the matrix to compute the cost of deletions,insertions and/or substitutions    
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0 # If the characters are the same in the two strings in a given position [i,j] then the cost is 0
            else:
                # In order to align the results with those of the Python Levenshtein package, if we choose to calculate the ratio
                # the cost of a substitution is 2. If we calculate just distance, then the cost of a substitution is 1.
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = min(distance[row-1][col] + 1,      # Cost of deletions
                                 distance[row][col-1] + 1,          # Cost of insertions
                                 distance[row-1][col-1] + cost)     # Cost of substitutions
    if ratio_calc == True:
        # Computation of the Levenshtein Distance Ratio
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t)) if (len(s) > 0 and len(t) > 0) or s == t else 0
        return Ratio
    else:
        # print(distance) # Uncomment if you want to see the matrix showing how the algorithm computes the cost of deletions,
        # insertions and/or substitutions
        # This is the minimum number of edits needed to convert string a to string b
        return distance[row][col]

def levenshtein_distance(s1, s2):
    # Calculate levenshtein distance between two strings
    return levenshtein_ratio_and_distance(s1, s2)

def levenshtein_ratio(s1, s2):
    # Calculate the similarity between two strings
    return levenshtein_ratio_and_distance(s1, s2, ratio_calc=True)

def find_function(module, target_function, fuzzy_threshold = 1):
    # Find a function in a module, that has the right signature, and the right name (or close to it)
    # fuzzy_threshold controlls how close the function names should match
    # target_function should have the same name, and parameters, as the expected function
    functions = get_module_functions(module)
    target_function_name = target_function.__name__.lower()
    target_function_arg_count = len(signature(target_function).parameters)

    for f in functions:
        if f.__name__.lower() == target_function_name and\
             len(signature(f).parameters) == target_function_arg_count:
            return f

    if fuzzy_threshold < 1:
        for f in functions:
            lev_ratio = levenshtein_ratio(target_function_name, f.__name__)
            if  lev_ratio > fuzzy_threshold and \
                    len(signature(f).parameters) == target_function_arg_count:
                return f
    return None

def process_result(result):
    # Count the number of different results by type
    count = len(result)
    passed = sum([1 for r in result if r[1] == PASS])
    failed = sum([1 for r in result if r[1] == FAIL])
    failed_error = sum([1 for r in result if EXCEPTION_TAG in r[1]])

    with open(Lookup.eval_feedback) as json_file:
        func_feedback = json.load(json_file)
    
    feedback = ""
    score = 1

    if passed == count: # If all tests passed
        return func_feedback[PASS], score
    else:   # If some tests failed
        feedback += func_feedback[FAIL]
        score = passed / count

    if failed_error > 0:    # If an exception was thrown, provide feedback on it.
        feedback += f"\n{func_feedback[EXCEPTION]}\n"

        errors = [(r[0], r[1].lstrip(EXCEPTION_TAG)) for r in result if EXCEPTION_TAG in r[1]]  # Extract all exceptions

        error_groups = {}       # Group exceptions by type
        for error in errors:
            error_groups[error[1]] = error_groups.get(error[1], []) + [error[0]]

        error_feedback = []

        for error, cases in error_groups.items():       # Decide if exception has occured multiple times, every time, or just once.
            if len(cases) >= count:                     # If the exception has occured in every case, probably means the code wasn't tested at all
                error_line = f"{error}: in every test case. You should see this error when you try to run your code"
            elif len(cases) > 1:                        # If an exception occures on more than one test case, probably means the code wasn't tested with various inputs
                error_line = f"{error}: in multiple different cases. Try testing your code with a few different inputs"
            else:                                       # If an exception occures only once, it means it was cought by an edge case tester. It's valuable to provide this, as it might help students understand their code better
                error_line = f"{error}: for one test case: {cases[0]}, you should check why this is."
            
            # Add contextual feedback per exception
            contextual_error_feedback = func_feedback['contextual']["exceptions"]
            if error in contextual_error_feedback:
                error_line += f"\n{contextual_error_feedback[error]}"
            error_feedback.append(error_line)
        feedback += '\n\n'.join(error_feedback)

    return feedback, score


def numbers_close(a, b, margin):
    return abs(a - b) < margin

def run_executable(executable, input_data, delay=0.2, timeout=10):
    # Run executable, wait a bit, than send input and return the decoded result split by line
    p = subprocess.Popen(executable, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(delay)
    try:
        result = p.communicate(input=input_data, timeout=timeout)[0]
    except subprocess.TimeoutExpired:
        result = b""
    p.kill()
    return result.decode('unicode_escape').replace("\r", "").split("\n")