# Your code here


def get_filename(path):
    return path.split("/")[-1]

def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    paths = {}
    for file in files:
        f = get_filename(file)
        if f not in paths:
            paths[f] = [file]

        else:
            paths[f].append(file)


    result = []
    for q in queries:
        f = get_filename(q)
        if f in paths:
            result.extend(paths[f])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
