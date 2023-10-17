def find_divider(num):
    count = 0
    result = []
    for i in range(1, num + 1):
        if num % i == 0:
            result.append(i)
            count += 1
    return result
