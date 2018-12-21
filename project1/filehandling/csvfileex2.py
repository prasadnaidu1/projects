import csv
with open('newemploee.txt','w') as fobj:
    writer=csv.writer(fobj,delimiter=':')
    writer.writerow(['firstname','lastname','age'])
    writer.writerow(['prasad', 'naidu', '34'])
    writer.writerow(['rajju', 'kumar', '30'])
    print()