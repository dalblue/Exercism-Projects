def istriangle(sides):
    triangular=False
    if sides!=[0,0,0]:
        if sides[0]+sides[1]>=sides[2] and sides[1]+sides[2]>=sides[0] and sides[0]+sides[2]>=sides[1]:
            triangular=True
    else:
        pass
    return triangular
        
    

def equilateral(sides):
    """
    determines if a triangle has sides of all equal lengths
    """
    if len(sides)!=3:
        raise ValueError("a triangle has 3 sides")
    isequal=False
    if not istriangle(sides):
        return isequal
    if sides[0]==sides[1] and sides[0]==sides[2] and sides[1]==sides[2]:
        isequal=True
    return isequal


def isosceles(sides):
    if len(sides)!=3:
        raise ValueError("a triangle has 3 sides")
    isiso=False
    if not istriangle(sides):
        return isiso
    if sides[0]==sides[1] and sides[0]!=sides[2]:
        isiso=True
    if sides[0]==sides[2] and sides[0]!=sides[1]:
        isiso=True
    if sides[1]==sides[2] and sides[1]!=sides[0]:
        isiso=True
    if equilateral(sides):
        isiso=True
    return isiso


def scalene(sides):
    if len(sides)!=3:
        raise ValueError("a triangle has 3 sides")
    isscalene=True
    if not istriangle(sides):
        isscalene=False
        return isscalene
    if equilateral(sides):
        isscalene=False
        return isscalene
        
    if sides[0]==sides[1] or sides[0]==sides[2] or sides[1]==sides[2]:
        isscalene=False
    return isscalene