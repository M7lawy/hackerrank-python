if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    summ = 0
    avg = 0
    
    if (student_marks[query_name]):
        summ += student_marks[query_name][0]
        summ += student_marks[query_name][1]
        summ += student_marks[query_name][2]
        
        avg = summ / 3
        print(f"{avg:.2f}")
    
    