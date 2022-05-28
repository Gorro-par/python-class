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
