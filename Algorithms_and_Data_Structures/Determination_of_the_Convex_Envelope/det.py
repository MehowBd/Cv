class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        pr = "(" + str(self.x) + ", " + str(self.y) + ")"
        return pr
    
def orientation(a: point, b: point, c: point):
    turn= (b.y-a.y)*(c.x-b.x) - (c.y-b.y)*(b.x-a.x)

    if turn == 0: #współliniowe
        return 0
    elif turn > 0: #prawoskrętne
        return 1
    elif turn < 0: #lewoskrętne
        return 2 
    
def is_between(a: point, b: point, c: point):
    if a.x == b.x == c.x:
        if b.y >= a.y and b.y <= c.y or b.y <= a.y and b.y >= c.y:
            return True
    if a.y == b.y == c.y:
        if b.x >= a.x and b.x <= c.x or b.x <= a.x and b.x >= c.x:
            return True
    
def jarvis_v1(points):
    n = len(points)
    if n < 0:
        return
    
    hull = []
    min_point = 0
    
    for i in range(1, len(points)):
        if points[i].x < points[min_point].x:
            min_point = i
        elif points[i].x == points[min_point].x:
            if points[i].y < points[min_point].y:
                min_point = i
    
    p = min_point
    hull.append(points[p])
    
    while True:
        
        q = (p + 1) % n
        
        for i in range(n):
            if orientation(points[p], points[q], points[i]) == 1:
                q = i
        p = q
        hull.append(points[p])

        if p == min_point:
            return hull
        
def jarvis_v2(points):
    n = len(points)
    if n < 0:
        return
    
    hull = []
    min_point = 0
    
    for i in range(1, len(points)):
        if points[i].x < points[min_point].x:
            min_point = i
        elif points[i].x == points[min_point].x:
            if points[i].y < points[min_point].y:
                min_point = i
    
    p = min_point
    hull.append(points[p])
    
    while True:
        
        q = (p + 1) % n
        
        for i in range(n):
            if orientation(points[p], points[q], points[i]) == 1:
                q = i
            if orientation(points[p], points[q], points[i]) == 0:
                if is_between(points[p], points[q], points[i]):
                    q = i
        p = q
        hull.append(points[p])

        if p == min_point:
            return hull


def main():
    punkty1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    points1 = []
    for punkt in punkty1:
        points1.append(point(punkt[0], punkt[1]))
        
    punkty2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
    points2 = []
    for punkt in punkty2:
        points2.append(point(punkt[0], punkt[1]))
    
    punkty3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    points3 = []
    for punkt in punkty3:
        points3.append(point(punkt[0], punkt[1]))
 
    print(jarvis_v1(points1))
    print(jarvis_v1(points2))
    print(jarvis_v1(points3))      
         
    print(jarvis_v2(points1))
    print(jarvis_v2(points2))
    print(jarvis_v2(points3))
    
    
    
    
    
if __name__ == "__main__":
    main()