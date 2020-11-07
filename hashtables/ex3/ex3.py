def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    arrays.sort(key = lambda x : len(x))

    dicts = [
        {ls: None for ls in array} for array in arrays
    ]

    counts = {}

    for a in dicts:
        for n in a.keys():
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1

    result = [k for k,v in counts.items() if v == len(arrays)]


    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
