if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    maxx = float('-inf')
    runnerUp = float('-inf')
    
    for i in range(n):
        if arr[i] > maxx:
            runnerUp = maxx     
            maxx = arr[i]       
        elif arr[i] < maxx and arr[i] > runnerUp:
            runnerUp = arr[i]   
            
    print(runnerUp)
        
