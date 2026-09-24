def score(x, y):
    points=0
    pointdistance=x**2+y**2
    if pointdistance>100:
        points=0
    if 25<pointdistance<=100:
        points=1
    if 1<pointdistance<=25:
        points=5
    if pointdistance<=1:
        points=10
    return points