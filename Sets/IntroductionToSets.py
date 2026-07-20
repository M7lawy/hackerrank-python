def average(array):
    
    summ = 0
    
    sett = set(array)
    
    for i in sett:
        summ += i
        
    
    return (summ / len(sett))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)