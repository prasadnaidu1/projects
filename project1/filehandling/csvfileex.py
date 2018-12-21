import  csv
with open("employee.csv","r") as fobj:
    lst=csv.reader(fobj,delimiter=':')
    for row in lst:
        for r in row:
            print(r,end='  ')
        print()