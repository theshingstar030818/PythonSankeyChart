import drawSvg as draw

d = draw.Drawing(200, 100, origin='center', displayInline=False)

# Draw an irregular polygon
d.append(draw.Lines(-80, -45,
                    70, -49,
                    95, 49,
                    -90, 40,
                    close=False,
            fill='#eeee00',
            stroke='black'))

# Draw a rectangle
d.append(draw.Rectangle(0,0,40,50, fill='#1248ff'))

# Draw a circle
d.append(draw.Circle(-40, -10, 30,
            fill='red', stroke_width=2, stroke='black'))

# Draw an arbitrary path (a triangle in this case)
p = draw.Path(stroke_width=2, stroke='green',
              fill='black', fill_opacity=0.5)
p.M(-30,5)  # Start path at point (-30, 5)
p.l(60,30)  # Draw line to (60, 30)
p.h(-70)    # Draw horizontal line to x=-70
p.Z()       # Draw line to start
d.append(p)

# Draw multiple circular arcs
d.append(draw.ArcLine(60,-20,20,60,270,
            stroke='red', stroke_width=5, fill='red', fill_opacity=0.2))
d.append(draw.Arc(60,-20,20,60,270,cw=False,
            stroke='green', stroke_width=3, fill='none'))
d.append(draw.Arc(60,-20,20,270,60,cw=True,
            stroke='blue', stroke_width=1, fill='black', fill_opacity=0.3))

# Draw arrows
arrow = draw.Marker(-0.1, -0.5, 0.9, 0.5, scale=4, orient='auto')
arrow.append(draw.Lines(-0.1, -0.5, -0.1, 0.5, 0.9, 0, fill='red', close=True))
p = draw.Path(stroke='red', stroke_width=2, fill='none',
              marker_end=arrow)  # Add an arrow to the end of a path
p.M(20, -40).L(20, -27).L(0, -20)  # Chain multiple path operations
d.append(p)
d.append(draw.Line(30, -20, 0, -10,
            stroke='red', stroke_width=2, fill='none',
            marker_end=arrow))  # Add an arrow to the end of a line

d.setPixelScale(2)  # Set number of pixels per geometry unit
#d.setRenderSize(400,200)  # Alternative to setPixelScale
d.saveSvg('example.svg')
d.savePng('example.png')

# Display in Jupyter notebook
d.rasterize()  # Display as PNG
d  # Display as SVG