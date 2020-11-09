def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    arr = []

    for i in range(0, len(arrays)):
        cache= {}
        for j in range(0, len(arrays[i])):
            cache[arrays[i][j]] = 1
        arr.append(cache)
    
    first_arr = arr[0]
    others_arr = arr[1:]
    for key in first_arr:
        add = True
        for cach in others_arr:
            if key not in cach:
                add = False
        if add:
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
