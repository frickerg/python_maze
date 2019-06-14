from itertools import groupby

# finds the shortest path which is merged from two given paths
def merge_to_shortest_path(a, b):
    # list of sequences, separated by occurence
    intersect_from_a = [list(g) for k, g in groupby(a, lambda x: x not in b)]
    intersect_from_b = [list(g) for k, g in groupby(b, lambda x: x not in a)]

    # create list of all steps of the shortest path
    merged_path = list()
    for i in range(len(intersect_from_a)):
        # if intersect sequences are equal, it can be added to merged_path
        if intersect_from_a[i] == intersect_from_b[i]:
            # append all steps without checking
            for step in intersect_from_a[i]:
                merged_path.append(step)
        else:
            # add all steps of the sequence that is shorter
            if len(intersect_from_a[i]) < len(intersect_from_b[i]):
                for step in intersect_from_a[i]:
                    merged_path.append(step)
            else:
                for step in intersect_from_b[i]:
                    merged_path.append(step)
    return merged_path
