def solution(array, height):
    i =0
    result =0
    for i in range(len(array)): 
        # 그냥 array로 돌아도 됐음.
        if array[i] > height:
        #그냥 i로 적어도 됐음.    
            result +=1
    return result
