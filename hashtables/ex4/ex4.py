def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for num in a:
        if num != 0:
            if num in cache:
                cache[num] += 1
            else:
                cache[num] = 1
                reverse = num * (-1)
                if reverse in cache:
                    if reverse > num:
                        result.append(reverse)
                    else:
                        result.append(num)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
