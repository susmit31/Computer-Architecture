def xor(a,b):
    out = ((not a) and b) or ((not b) and a)
    return int(out)

def new_carry(a,b,c):
    return int(a*b or b*c or c*a)

def fill_zeros(a,b):
    if len(a) > len(b):
        while len(a) > len(b):
            b = '0' + b
    else:
        while len(b) > len(a):
            a = '0' + a
    return a,b

def adder(a,b):
    a,b = str(a), str(b)
    a, b = fill_zeros(a,b)
    a = [int(bit) for bit in a[::-1]]
    b = [int(bit) for bit in b[::-1]]
    sum = ''
    carry = 0
    for i in range(len(a)):
        sbit = xor(a[i],b[i])
        sbit = xor(sbit, carry)
        carry = new_carry(a[i],b[i],carry)
        sum = f'{sbit}{sum}'
    sum = f'{carry}{sum}' if carry else sum
    return int(sum)

def b2d(b):
    b = str(b)[::-1]
    d = 0
    for i,bit in enumerate(b):
        d += int(bit)*2**i
    return d

def d2b(d):
    b = ''
    while d>=1:
        b = str(d%2)+b
        d = d//2
    return int(b)