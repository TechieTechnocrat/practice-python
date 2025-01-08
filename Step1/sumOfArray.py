def simpleArraySum(ar):
    sum = 0
    for x in ar:
        sum = sum + x
    return sum


hey_list = [10, 20, 90, 1000]
result = simpleArraySum(hey_list)
print(result)