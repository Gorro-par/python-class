def sumvalue(value, **kwargs):
    hap = value
    for key in kwargs:
        hap += kwargs[key]
    return hap

coffeeprint = {'에소프레소':2500, '아메리카노':2800, '카페라테':3200}
print(sumvalue(1000, **coffeeprint))
print(sumvalue(value = 2000, **coffeeprint))
print(sumvalue(**coffeeprint, value = 2000))

