def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    positive = {n:None for n in a if n > 0}
    negative = {n:None for n in a if n < 0}
    
    result = [n for n in positive if -n in negative]

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
