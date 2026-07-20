if __name__ == '__main__':
    
    n = int(input())
    students = []
    
    for _ in range(n):
        name = input()
        score = float(input())
        
        students.append([name , score])
        
    minScore = float("inf")
    
    
    def getMin():
        
        global minScore
        minScore = float("inf")
        
        for i in range(len(students)):
            if students[i][1] < minScore:
                minScore = students[i][1]    
      
       
    
    getMin()
    
    for student in students.copy():
        if student[1] == minScore:
            students.remove(student)
            
    getMin()
    
    lastList = []
    
    for i in range(len(students)):
        if students[i][1] == minScore:
            lastList.append([students[i][0], students[i][1]])
            
    lastList.sort()
    
    for i in range(len(lastList)):
        print(lastList[i][0])
    
    
        
        
    
        
    
        
        
        
        
