if __name__ == '__main__':
    mlist=[]
    sublist=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        sublist= [name,score]
        mlist.append(sublist)


    students = mlist
        #print(students[1])
        #print(students[1][1])
        #print(students.__len__())
    len =students.__len__()
    min1 = students[len-1][1]
    min2 = students[len-1][1]
    for i in range(students.__len__()):
        if(students[i][1]==min2):
               continue
        if(students[i][1]<=min2):
             min1=min2
             min2=students[i][1]
        elif(students[i][1]<=min1):
            min1=students[i][1]
    
   
    students.sort(key=None, reverse=False)
    for i in range(students.__len__()):
        if(students[i][1]==min1):
            print(students[i][0])