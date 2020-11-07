def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    w_dict = {v:i for i,v in sorted(enumerate(weights), key = lambda item: item[0], reverse= True)}

    if len(w_dict) != length:
        w_dict = {}
        for i,v in enumerate(weights):
            if v not in w_dict:
                w_dict[v] = [i]

            else:
                w_dict[v].append(i)
        for v, l in w_dict.items():
            diff = limit - v
            if diff in w_dict:
                if len(l) > 1:
                    return(l[1], l[0])
    else:
        for v, i in w_dict.items():
            diff = limit - v
            print(f"{limit} - {v} = {diff}")
            print(diff in w_dict)
            if diff in w_dict:
                return (i, w_dict[diff])

if __name__ == "__main__":
        weights_2 = [4, 4]
        answer = get_indices_of_item_weights(weights_2, 2, 8)
        print(answer)