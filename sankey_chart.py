import drawSvg as draw
import pandas as pd
from PIL import Image


df = pd.DataFrame([[15.7, 11.9, 3.8]], index=[1], columns=['Comp', 'Traffic', 'Ticket'])
# df = pd.DataFrame([[9.0, -2.0, 11.1]], index=[1], columns=['Comp', 'Traffic', 'Ticket'])

comp_val = df.at[1, 'Comp']
traffic_val = df.at[1, 'Traffic']
ticket_val = df.at[1, 'Ticket']

traffic_h = abs(traffic_val)/(abs(traffic_val) + abs(ticket_val))
ticket_h = abs(ticket_val)/(abs(traffic_val) + abs(ticket_val))


w = 1200
h = 800
r = 1.0
d = draw.Drawing(w, h, origin='center', displayInline=False)

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

if h1 < bh/5.0:
    delta_y = h1 * 0.2
else:
    delta_y = h1 * 0.1

if traffic_h < ticket_h:
    delta_y = delta_y * -1.0

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
space_h = 2*r
w1 = bw
h1 = bh


x1 = bx + w1 * r
y1 = by + bh*ticket_h * r - space_h

# d.append(draw.Circle(x1,y1, 30,
#             fill='red', stroke_width=2, stroke='black'))

w1 = bw
h1 = bh*ticket_h-space_h
if h1 < bh/5.0:
    delta_y = h1 * 0.2
else:
    delta_y = h1 * 0.1

if traffic_h < ticket_h:
    delta_y = delta_y * -1.0



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

d.saveSvg('1.svg')
d.savePng('1.png')

# img = Image.open('1.png')
# img.show()
d.rasterize()  # Display as PNG
