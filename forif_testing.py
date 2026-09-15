mags=[5.2,6.8,3.1,7.5,4.4,6.1]
total=0.0
for m in mags:
    total=total+m
avg=total/len(mags)
print("平均震级：",avg)
