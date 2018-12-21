try:
    marks_list=[67,89,89]
    assert len(marks_list)!=0,'marks list is empty'
    avg=sum(marks_list)//len(marks_list)
    print('average marks:',avg)
except AssertionError as ae:
    print('Assertation Error:',ae)

