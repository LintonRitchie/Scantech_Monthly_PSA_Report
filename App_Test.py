from datetime import datetime
from dateutil.relativedelta import relativedelta
given_date = '21/1/2021'
print('Give Date: ', given_date)
date_format = '%d/%m/%Y'
dtObj = datetime.strptime(given_date, date_format)
future = dtObj + relativedelta(months=-1)
print(future)
print(future.strftime("%B"))
print(datetime.today().strftime("%d %B %Y"))