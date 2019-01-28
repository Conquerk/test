import numpy as np

data = [('zs',[10,15,2],3),
        ('ls',[12,15,92],13),
        ('ww',[14,35,22],43)]
#第一种设置dtype的方式
a = np.array(data,dtype='U2,3int32,int32')
print(a,'zs.age:',a[0]['f1'])
#第二种设置dypte的方式
b = np.array(data,dtype=[
            ('name','str_',2),
            ('scores','int32',3),
            ('age','int32',1)])
print(b,'ww.age:',b[2]['age'])
#第三种设置dtype的方式
c = np.array(data,dtype={
    'names':['name','score','age'],
    'formats':['U2','3int32','int32']})    
print(c,'ls.name:',c[1]['name'])
#第四种设置方式
d = np.array(data,dtype={
    'name':('U2',0),
    'scores':('3int32',16),
    'age':('int32',28)
})
#第五种dtype的设置方式
e = np.array([0x1234,0x5678],
        dtype=('u2',
        {'lowc':('u1',0),'highc':('u1',1)}))
print('%x'%e[0])
print('%x'%e['lowc'][0])
print('%x'%e['highc'][0])
