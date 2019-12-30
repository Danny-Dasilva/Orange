
def convert(obj):
    print(obj)

    a, b, c, d = obj[0], obj[1], obj[2], obj[3]

    svg = f'<svg height="480" width="640"> <polygon points="{a[0]},{a[1]} {b[0]},{b[1]} {c[0]},{c[1]} {d[0]},{d[1]}" style="fill:none;stroke:orange;stroke-width:1" /> Sorry, your browser does not support inline SVG. </svg>'

    return svg


