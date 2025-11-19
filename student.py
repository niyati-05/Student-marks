import sys

if len(sys.argv)== 4:
    system_name = sys.argv[0]
    student_name = sys.argv[1]
    marks1 = sys.argv[2]
    marks2 = sys.argv[3]

else:
    system_name = sys.argv[0]
    student_name = "Niyati"
    marks1 = "18" 
    marks2 = "20"

average_score = (int(marks1) + int(marks2)) / 2
print(f"Average internal score is {average_score}")