"""
作者:潮圆信寂
时间:未定
版权所有,侵权必究.
"""
sandwich_orders = ['Sandwiches1','Sandwiches2','Sandwiches3','Sandwiches4']
finished_sandwiches = []
for i in sandwich_orders:
    print('I made your ' +i+' sandwich')
    finished_sandwiches.append(i)
print('I made ',finished_sandwiches,' in total!')
print('\n')
for i in range(1,4):
    sandwich_orders.append('pastrami')
print(sandwich_orders)
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
print('pastrami is sold out!')
finished_sandwiches=sandwich_orders
print(finished_sandwiches)