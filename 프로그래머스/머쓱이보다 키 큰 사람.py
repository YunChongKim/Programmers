def solution(array, height):
    i =0
    result =0
    for i in range(len(array)):
        if array[i] > height:
            result +=1
    return result
