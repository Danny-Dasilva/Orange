
def convert(obj):
    print(obj)
    a, b, c, d = obj[0], obj[1], obj[2], obj[3]
    print(a, b, c, d, "abbbb")

    svg = f'<svg height="480" width="640"> <polygon points="{a[0]},{a[1]} {b[0]},{b[1]} {c[0]},{c[1]} {d[0]},{d[1]}" style="fill:none;stroke:orange;stroke-width:1" /> Sorry, your browser does not support inline SVG. </svg>'

    print(svg)
   # x0, y0, x1, y1 = obj.bounding_box.flatten().tolist()
    #print(x0,y0,x1,y1, "cordinates")



