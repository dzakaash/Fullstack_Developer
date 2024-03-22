def equality(data):
    data_unq = list(set(data))
    count_data = 0
    for i in range(len(data_unq)):
        count = 0
        for j in range(len(data)):
            if data_unq[i] == data[j]:
                count += 1
        if count > count_data:
            count_data = count
    result = len(data) - count_data
    return print({"result": result})

equality([3, 3, 2, 1, 3])