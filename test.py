a_list = ["1", "2", "3"]
print('-'.join(a_list))

print('{2} - {0} - {1}'.format(1, 2, 3))

# print('{:d}'.format(2.5))

print('{:*^10}'.format('prueba'))

nro_cuenta = '32673'

saldo = 100.2543

print('El saldo de la cuenta {:s} es ${:.2f}'.format(nro_cuenta, saldo))
print('El saldo de la cuenta {:} es ${:.2f}'.format(nro_cuenta, saldo))



import datetime


# print(datetime.datetime(2019, 1, 1, 12, 10, 35))
# print(datetime.datetime(2019, 2, 29))
print(datetime.datetime.today())
print(datetime.datetime.today() - datetime.timedelta(days=1))
print(datetime.date.today() - datetime.timedelta(days=1))
print(datetime.datetime.now() - datetime.timedelta(days=1))
print(datetime.date.today() - datetime.timedelta(seconds=86900))
print(datetime.date.today() - datetime.timedelta(seconds=86390))

# date = datetime.datetime

# print(datetime.date(2019, 12, 31).isoformat())
#
# date_time = datetime.datetime(2019, 2, 27, 11, 15, 30)
# print(date_time.strftime('%d/%m/%y %H:%M'))

# date_time = '2019-01-30 15:30:45'
# print(date_time.strftime('%Y-%m-%d %H:%M:%S'))
# print(date_time.strptime('%Y-%m-%d %H:%M:%S'))
# print(datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S'))
# print(datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S.%f'))

date_time = datetime.datetime(2010, 8, 25, 10, 35, 15)
print(date_time.strftime('%Y/%m/%d %H:%M:%S'))