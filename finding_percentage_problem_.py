from audioop import avg
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
   # print(student_marks)
    query_name = input()

#     thisdict =    {
#       "apple": [12,23,34,45],
#       "banana": [12,23,34,45],
#       "cherry": [12,23,34,45]
#     }
#     
#     
#     thisdict["orange"] = [12,23,34,45]
#     
#     
#     print(thisdict)
#     print(thisdict["apple"][0])

#print(student_marks[query_name])
avg=0.0
for i in range(len(student_marks[query_name])):
   avg += student_marks[query_name][i]
 #  print(avg)

print("%.2f" % (avg/len(student_marks[query_name])))
