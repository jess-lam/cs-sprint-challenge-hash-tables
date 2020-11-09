
cache = {}
def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    for i in range(0, len(weights)):
        x = limit - weights[i]
        if x in cache:
            if cache[x] > i:
                return[cache[x], i]
            else:
                return [i, cache[x]]
        else:
            cache[weights[i]] = i
    return None




