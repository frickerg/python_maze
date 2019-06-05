from itertools import groupby


def merge_to_shortest_path(a, b):
    intersect_from_a = [list(g) for k, g in groupby(a, lambda x: x not in b)]
    intersect_from_b = [list(g) for k, g in groupby(b, lambda x: x not in a)]

    merged_path = list()
    for i in range(len(intersect_from_a)):
        if intersect_from_a[i] == intersect_from_b[i]:
            for step in intersect_from_a[i]:
                merged_path.append(step)
        else:
            if len(intersect_from_a[i]) < len(intersect_from_b[i]):
                for step in intersect_from_a[i]:
                    merged_path.append(step)
            else:
                for step in intersect_from_b[i]:
                    merged_path.append(step)
    return merged_path
