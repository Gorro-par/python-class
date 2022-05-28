
def hello(name):
    print('안녕, {}!'.format(name))

hello('수빈')
sname = '현수'
hello(sname)


def hello(name = '여러분'):
    print('안녕, {}!'.format(name))

hello()
hello('헌철')


def mysum(x, y = 0):
    return x + y

hap = mysum(5)
print(hap)
hap = mysum(5, 10)
print(hap)

#
def ctofatrenhite(cels):
    return cels * 9/5 + 32

def ftocelsius(fahr):
    return (fahr - 32) * 5/9

for cels in range(28, 35, 2):
    print('섭씨" {}, 화씨: {:.2f}'.format(cels, ctofatrenhite(cels)))


for fahr in range(90,103, 3):
    print('섭씨" {:.2f}, 화씨: {}'.format(ftocelsius(fahr), fahr))


def addone():
    i = 30
    i += 1
    print('\t지역변수 i:',i)

i = 20
print('i:',i)
addone()
print('i',i)


def addone():
    print('\t 전역 변수 i 읽기, i + 1: ', i + 1)

i = 20
print('i = ', i)
addone()
print('i = ', i)


# def addone():
#     global i
#     print('t\ 전역 변수 i 읽기 i + 1 ', i + 1)
#     i += 1
#
# i = 20
# print('i = ', i)
# addone()
# print('i = ', i)

def hello(*names):
    for each in names:
        print('안녕, {}!'.format(each))

hello('나타샤')
hello('수빈', '현수', '지효')
hello(*['방탄소년단', '여자친구'])


def mykeyprint(**kwargs):
    for key in kwargs:
        print('{}: {} '.format(key, kwargs[key]), end = ' ')
    print()


mykeyprint(여자친구=6, 마마무=4)
mykeyprint(엑소=9, 트와이스=9, 블랙핑크=4, 방탄소년단=7)

coffeeprint = {'에소프레소':2500, '아메리카노':2800, '카페라테':3200}
mycar = {"brand": "현대", "model":"제네시스", "year":2016}
mykeyprint(**coffeeprint)
mykeyprint(**mycar)




#
def sumvalue(value, **kwargs):
    hap = value
    for key in kwargs:
        hap += kwargs[key]
    return hap

coffeeprint = {'에소프레소':2500, '아메리카노':2800, '카페라테':3200}
print(sumvalue(1000, **coffeeprint))
print(sumvalue(value = 2000, **coffeeprint))
print(sumvalue(**coffeeprint, value = 2000))




def sumvalue(*values, **kwargs):
    hap = 0
    for v in values:
        hap += v
    for key in kwargs:
        hap += kwargs[key]
    return hap

coffeeprint = {'value': 2000, '에소프레소':2500, '아메리카노':2800, '카페라테':3200}
print(sumvalue(1,2,3,**coffeeprint))
print(sumvalue(*[2, 3, 4], **coffeeprint))
