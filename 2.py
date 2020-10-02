import drawSvg as draw
import pandas as pd

# >>> df = pd.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
# ...                   index=[4, 5, 6], columns=['A', 'B', 'C'])
# >>> df
#     A   B   C
# 4   0   2   3
# 5   0   4   1
# 6  10  20  30
df = pd.DataFrame([[15.7, 11.9, 3.8]], index=[1], columns=['Comp', 'Traffic', 'Ticket'])

# comp_val = 15.7
# traffic_val = 11.9
# ticket_val = 3.8
comp_val = df.at[1, 'Comp']
traffic_val = df.at[1, 'Traffic']
ticket_val = df.at[1, 'Ticket']

traffic_h = abs(traffic_val)/(abs(traffic_val) + abs(ticket_val))
ticket_h = abs(ticket_val)/(abs(traffic_val) + abs(ticket_val))


w = 1200
h = 800
r = 1.0
d = draw.Drawing(w, h, origin='center', displayInline=False)

# function drawAnRect(x1, y1, x2, y2, x3, y3, x4, y4, is_closed=True, fill_color, txt, txt_color='black', txt_x1, txt_x2)
# Draw an irregular polygon

# 2f6fc7
# 3e87c1
# 87b7df
# red
# ca352f
# da7879

########### draw Comp #############
bx = -300
by = -75
bw = 200
bh = 300

w1 = bw
h1 = bh
d.append(draw.Rectangle(bx+0*r, by+0*r, w1*r, h1*r, fill='#2f6fc7'))

# d.append(draw.Circle(bx+0*r, by+0*r, 30,
#             fill='yellow', stroke_width=2, stroke='black'))


x2 = bx + w1/2.0 * r
y2 = by + h1/2.0 * r
txt = 'Comp%'
d.append(draw.Text(txt, 15, x2, y2, center=0.5, fill='white'))

x2 = bx + w1/2.0 * r
y2 = by + h1/2.0 * r
txt = str(comp_val) + '%'
d.append(draw.Text(txt, 15, x2, y2, center=3.5, fill='white'))


########### draw Traffic #############
x1 = bx + w1 * r
y1 = by + h1 * r

w1 = bw
h1 = bh*traffic_h
delta_y = h1*0.1

if traffic_val >= 0:
    fill_color = '#3e87c1'
else:
    fill_color = '#ca352f'

d.append(draw.Lines(x1, y1,
                    x1 + w1*r, y1+delta_y*r,
                    x1 + w1*r, y1-h1*r+delta_y*r,
                    x1, y1-h1*r,
                    close=True,
            fill=fill_color,
            stroke=fill_color))

x2 = x1 + w1/2.0 * r
y2 = y1 - h1/2.0 * r
txt = 'Traffic%'
d.append(draw.Text(txt, 15, x2, y2, center=0.5, fill='white'))

########### draw Traffic percent #############
x1 = x1 + w1 * r
y1 = y1 + delta_y

w1 = bw * 0.7
h1 = bh * traffic_h
delta_y = h1*0.2
if traffic_val >= 0:
    fill_color = '#87b7df'
else:
    fill_color = '#da7879'

d.append(draw.Lines(x1, y1,
                    x1 + w1*r, y1,
                    x1 + w1*r, y1-h1*r,
                    x1, y1-h1*r,
                    close=True,
            fill=fill_color,
            stroke=fill_color))

x2 = x1 + w1/2.0 * r
y2 = y1 - h1/2.0 * r
txt = str(traffic_val) + '%'
if traffic_val >= 0:
    fill_color = 'black'
else:
    fill_color = 'white'
d.append(draw.Text(txt, 15, x2, y2, center=0.5, fill=fill_color))

########### draw Ticket #############
space_h = 5*r
w1 = bw
h1 = bh


x1 = bx + w1 * r
y1 = by + bh*ticket_h * r - 5*r

# d.append(draw.Circle(x1,y1, 30,
#             fill='red', stroke_width=2, stroke='black'))

w1 = bw
h1 = bh*ticket_h-space_h
delta_y = h1*0.2
if ticket_val >= 0:
    fill_color = '#3e87c1'
else:
    fill_color = '#ca352f'

d.append(draw.Lines(x1, y1,
                    x1 + w1*r, y1+delta_y*r,
                    x1 + w1*r, y1-h1+delta_y*r,
                    x1, y1-h1*r,
                    close=True,
            fill=fill_color,
            stroke=fill_color))

x2 = x1 + w1/2.0 * r
y2 = y1 - h1/2.0 * r
txt = 'Ticket%'
d.append(draw.Text(txt, 15, x2, y2, center=0.5, fill='white'))

########### draw Ticket percent #############
x1 = x1 + w1 * r
y1 = y1 + delta_y

w1 = bw * 0.7
h1 = bh * ticket_h-space_h
if ticket_val >= 0:
    fill_color = '#87b7df'
else:
    fill_color = '#da7879'

d.append(draw.Lines(x1, y1,
                    x1 + w1*r, y1,
                    x1 + w1*r, y1-h1*r,
                    x1, y1-h1*r,
                    close=True,
            fill=fill_color,
            stroke=fill_color))

x1 = x1 + w1/2.0 * r
y1 = y1 - h1/2.0 * r
txt = str(ticket_val) + '%'
if ticket_val >= 0:
    fill_color = 'black'
else:
    fill_color = 'white'
d.append(draw.Text(txt, 15, x1, y1, center=0.5, fill=fill_color))



# x1 = bx + w1/2.0 * r
# y1 = by + h1/2.0 * r
# txt = str(comp_val) + '%'
# d.append(draw.Text(txt, 15, x1, y1, center=3.5, fill='white'))


# d.append(draw.Text('Comp%',insert = (30, 55),font_size="10px",fill='black'))
# dwg.add(dwg.text('Test',insert = (30, 55),font_size="10px",fill='black'))

# hlink.append(draw.Text('Hyperlink',0.2, 0,0, center=0.6, fill='white'))


# d.append(draw.Rectangle(0*r, 0*r, 100*r, 150*r, fill='#2f6fc7'))

# d.setPixelScale(1)  # Set number of pixels per geometry unit
#d.setRenderSize(400,200)  # Alternative to setPixelScale
d.saveSvg('example.svg')
d.savePng('example.png')

# Display in Jupyter notebook
d.rasterize()  # Display as PNG
d  # Display as SVG

# d.append(draw.Lines(0*r, 0*r,
#                     100*r, 0*r,
#                     100*r, 150*r,
#                     0*r, 150*r,
#                     close=True,
#             fill='#eeee00',
#             stroke='black'))
#
# # Draw a rectangle
# d.append(draw.Rectangle(0,0,40,50, fill='#1248ff'))
#
# # Draw a circle
# d.append(draw.Circle(-40, -10, 30,
#             fill='red', stroke_width=2, stroke='black'))
#
# # Draw an arbitrary path (a triangle in this case)
# p = draw.Path(stroke_width=2, stroke='green',
#               fill='black', fill_opacity=0.5)
# p.M(-30,5)  # Start path at point (-30, 5)
# p.l(60,30)  # Draw line to (60, 30)
# p.h(-70)    # Draw horizontal line to x=-70
# p.Z()       # Draw line to start
# d.append(p)
#
# # Draw multiple circular arcs
# d.append(draw.ArcLine(60,-20,20,60,270,
#             stroke='red', stroke_width=5, fill='red', fill_opacity=0.2))
# d.append(draw.Arc(60,-20,20,60,270,cw=False,
#             stroke='green', stroke_width=3, fill='none'))
# d.append(draw.Arc(60,-20,20,270,60,cw=True,
#             stroke='blue', stroke_width=1, fill='black', fill_opacity=0.3))
#
# # Draw arrows
# arrow = draw.Marker(-0.1, -0.5, 0.9, 0.5, scale=4, orient='auto')
# arrow.append(draw.Lines(-0.1, -0.5, -0.1, 0.5, 0.9, 0, fill='red', close=True))
# p = draw.Path(stroke='red', stroke_width=2, fill='none',
#               marker_end=arrow)  # Add an arrow to the end of a path
# p.M(20, -40).L(20, -27).L(0, -20)  # Chain multiple path operations
# d.append(p)
# d.append(draw.Line(30, -20, 0, -10,
#             stroke='red', stroke_width=2, fill='none',
#             marker_end=arrow))  # Add an arrow to the end of a line
#
# d.setPixelScale(2)  # Set number of pixels per geometry unit
# #d.setRenderSize(400,200)  # Alternative to setPixelScale
# d.saveSvg('example.svg')
# d.savePng('example.png')
#
# # Display in Jupyter notebook
# d.rasterize()  # Display as PNG
# d  # Display as SVG