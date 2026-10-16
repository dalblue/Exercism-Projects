def score(point1, point2):
    points=0
    pointdistance=point1**2+point2**2
    if pointdistance>100:
        points=0
    if 25<pointdistance<=100:
        points=1
    if 1<pointdistance<=25:
        points=5
    if pointdistance<=1:
        points=10
    return points