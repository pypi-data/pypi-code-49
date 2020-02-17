from nada_dataprofilering.exceptions.vizualisation_exceptions import VizualKeysNotFound


def make_table_data(response, threshold=10):

    response_sorted = sort_resp(response)

    values = response_sorted['VERDI']
    counts = response_sorted['ANTALL']

    for i in range(len(values)):
        try:
            values[i] = values[i].strftime('%d-%m-%Y')
        except AttributeError:
            pass

    if len(values) > threshold:
        new_counts = counts[:threshold-1]
        new_values = values[:threshold - 1]

        new_counts.append(sum(counts[threshold - 1:]))
        new_values.append('Andre')
    else:
        new_counts = counts
        new_values = values

    return [[new_values[i], new_counts[i]] for i in range(len(new_values))]


def sort_resp(resp):
    try:
        values = resp['VERDI']
        counts = resp['ANTALL']

    except KeyError:
        raise VizualKeysNotFound(f"Expected ['VERDI', 'ANTALL'] as keys but got {list(resp.keys())}")

    new_counts, new_values = (list(t) for t in zip(*sorted(zip(counts, values), reverse=True)))
    return {'VERDI': new_values, 'ANTALL': new_counts}
