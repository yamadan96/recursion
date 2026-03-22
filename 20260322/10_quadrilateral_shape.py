def getShapeType(ax, ay, bx, by, cx, cy, dx, dy):
    A, B, C, D = (ax,ay), (bx,by), (cx,cy), (dx,dy)
    points = [A, B, C, D]

    # 外積（3点の位置関係を判定）
    def cross(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

    # 重複チェック
    for i in range(4):
        for j in range(i+1, 4):
            if points[i] == points[j]:
                return "not a quadrilateral"

    # 3点が一直線上にあるかチェック
    for i in range(4):
        for j in range(i+1, 4):
            for k in range(j+1, 4):
                if cross(points[i], points[j], points[k]) == 0:
                    return "not a quadrilateral"

    # 自己交差チェック（対辺が交差していないか）
    def on_segment(p, q, r):
        return (min(p[0],r[0]) <= q[0] <= max(p[0],r[0]) and
                min(p[1],r[1]) <= q[1] <= max(p[1],r[1]))

    def segments_intersect(p1, p2, p3, p4):
        d1, d2 = cross(p3, p4, p1), cross(p3, p4, p2)
        d3, d4 = cross(p1, p2, p3), cross(p1, p2, p4)
        if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and \
           ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
            return True
        if d1 == 0 and on_segment(p3, p1, p4): return True
        if d2 == 0 and on_segment(p3, p2, p4): return True
        if d3 == 0 and on_segment(p1, p3, p2): return True
        if d4 == 0 and on_segment(p1, p4, p2): return True
        return False

    if segments_intersect(A, B, C, D) or segments_intersect(B, C, D, A):
        return "not a quadrilateral"

    # 辺の長さ（二乗）
    ab = (bx-ax)**2 + (by-ay)**2
    bc = (cx-bx)**2 + (cy-by)**2
    cd = (dx-cx)**2 + (dy-cy)**2
    da = (ax-dx)**2 + (ay-dy)**2

    # 対角線の長さ（二乗）
    ac = (cx-ax)**2 + (cy-ay)**2
    bd = (dx-bx)**2 + (dy-by)**2

    # 平行チェック
    def is_parallel(p1, p2, p3, p4):
        return (p2[0]-p1[0])*(p4[1]-p3[1]) - (p2[1]-p1[1])*(p4[0]-p3[0]) == 0

    ab_cd = is_parallel(A, B, C, D)  # AB || CD
    bc_da = is_parallel(B, C, D, A)  # BC || DA

    all_equal = (ab == bc == cd == da)

    # 判定（優先順位順）
    if all_equal and ac == bd:
        return "square"
    if all_equal:
        return "rhombus"
    if ab_cd and bc_da:
        return "parallelogram"
    if ab_cd or bc_da:
        return "trapezoid"
    if (ab == bc and cd == da) or (ab == da and bc == cd):
        return "kite"
    return "other"


# テスト
print(getShapeType(1,1,2,2,3,3,4,4))             # not a quadrilateral
print(getShapeType(1,1,2,2,3,3,-1,-1))            # not a quadrilateral
print(getShapeType(0,0,1,1,0,0,1,1))              # not a quadrilateral
print(getShapeType(0,0,1,0,1,1,4,-5))             # other
print(getShapeType(0,0,0,1,1,1,0,0))              # not a quadrilateral
print(getShapeType(0,2,2,2,2,4,0,4))              # square
print(getShapeType(3,3,3,-3,-3,-3,-3,3))          # square
print(getShapeType(0,0,5,5,10,0,5,-5))            # square
print(getShapeType(0,0,5,0,8,4,3,4))              # rhombus
print(getShapeType(-1,2,8,5,5,-4,-4,-7))          # rhombus
print(getShapeType(-1,5,3,3,6,-4,2,-2))           # parallelogram
print(getShapeType(-4,3,5,6,2,-2,-7,-5))          # parallelogram
print(getShapeType(-2,0,5,0,8,8,-1,8))            # trapezoid
print(getShapeType(-1,5,-3,1,3,-2,3,3))           # trapezoid
print(getShapeType(-3,3,1,5,4,-1,1,-5))           # trapezoid
print(getShapeType(0,0,5,3,0,8,-5,3))             # kite
print(getShapeType(-5,7,2,6,5,-3,-4,0))           # kite
print(getShapeType(-1,5,3,1,-1,-1,-5,1))          # kite
print(getShapeType(0,1,2,3,3,4,2,1))              # not a quadrilateral
print(getShapeType(-2,1,2,6,3,4,4,2))             # not a quadrilateral
print(getShapeType(-3,0,-2,6,-1,2,-2,1))          # not a quadrilateral
print(getShapeType(0,0,8,0,10,12,2,6))            # other
print(getShapeType(-2,5,4,2,4,-4,-4,-4))          # other
print(getShapeType(0,0,1,2,3,2,1,1))              # other
