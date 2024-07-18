import modLib as ml

print(ml.gcd(606, 660))
d = ml.Extended_Euclidian_Algorithm(38993, 606*660)[0]
if d < 0:
    d += 606*660
print(d)
print(d*38993 % (606*660))