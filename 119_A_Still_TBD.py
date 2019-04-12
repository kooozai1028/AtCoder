import datetime

date = datetime.datetime.strptime(input(),'%Y/%m/%d')
cri_date = datetime.datetime(2019,4,30)

if date <= cri_date:
    print('Heisei')
else:
    print('TBD')