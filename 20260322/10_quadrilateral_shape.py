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

    # 自己交差チェック（交差していたらother）
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
        return "other（その他）"

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
        return "square（正方形）"
    if all_equal:
        return "rhombus（ひし形）"
    if ab_cd and bc_da and ac == bd:
        return "rectangle（長方形）"
    if ab_cd and bc_da:
        return "parallelogram（平行四辺形）"
    if ab_cd or bc_da:
        return "trapezoid（台形）"
    if (ab == bc and cd == da) or (ab == da and bc == cd):
        return "kite（凧）"
    return "other（その他）"


# テスト
print(getShapeType(1,1,2,2,3,3,4,4))             # not a quadrilateral
print(getShapeType(0,2,2,2,2,4,0,4))              # square（正方形）
print(getShapeType(0,0,5,0,8,4,3,4))              # rhombus（ひし形）
print(getShapeType(738,463,738,335,392,335,392,463))  # rectangle（長方形）
print(getShapeType(-1,5,3,3,6,-4,2,-2))           # parallelogram（平行四辺形）
print(getShapeType(-2,0,5,0,8,8,-1,8))            # trapezoid（台形）
print(getShapeType(0,0,5,3,0,8,-5,3))             # kite（凧）
print(getShapeType(0,0,1,0,1,1,4,-5))             # other（その他）
print(getShapeType(458,968,458,145,738,968,738,563))  # other（その他）
