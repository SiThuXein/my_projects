from tkinter import *
from tkinter import ttk

root = Tk()

class Mybutton(Button):
    def __init__(self, parent, **a):
        super().__init__(parent, **a)
        self.config(command = self.click)

    def click(self):
        s1 = str(lb1['text'])
        s2 = str(self['text'])
        if s2 == 'CE':
            lb1.config(text = 0)
        elif s2 == '\u232B':
            if '.' in s1:
                lb1.config(text = s1[:-1] if len(s1) > 1 else 0)
            else:
                lb1.config(text = int(s1[:-1]) if len(s1) > 1 else 0)
        elif s2 == '.':
            if '.' not in s1:
                lb1.config(text = s1 + s2)
        else:
            if '.' in s1:
                lb1.config(text = s1 + s2)
            else:
                lb1.config(text = int(s1 + s2))
        self.convert()

    def convert(self):
        from_value = str(lb1['text'])
        if '.' in from_value:
            from_value = float(from_value)
        else:
            from_value = int(from_value)

        values = {
            'Meters':{
                'Centimeters': from_value * 100,
                'Feet': from_value * 3,
                'Inches': from_value * 39.37008,
                'Yards': from_value * 1,
                'Miles': 0.000621
            },
            'Centimeters':{
                'Meters': from_value / 100,
                'Feet': from_value * 0.032808,
                'Inches': from_value * 0.393701,
                'Yards': from_value * 0.010936,
                'Miles': from_value * 0.0000062137
            },
            'Feet':{
                'Meters': from_value * 0.3048,
                'Cenitemeters': from_value * 30.48,
                'Inches': from_value * 12,
                'Yards': from_value / 3,
                'Miles': from_value * 0.000189
            },
            'Inches':{
                'Meters': from_value * 0.0254,
                'Centimeters' : from_value * 2.54,
                'Feet': from_value / 12,
                'Yards': from_value / 36,
                'Miles': from_value * 0.000016 
            },
             'Yards':{
                'Meters': from_value * 0.9144,
                'Centimeters' : from_value * 91.44,
                'Feet': from_value * 3,
                'Inches': from_value * 36,
                'Miles': from_value / 1760
            },
             'Miles':{
                'Meters': from_value * 1609.344,
                'Centimeters' : from_value * 160934.4,
                'Feet': from_value * 5280,
                'Yards': from_value * 1760,
                'Inches': from_value * 63360
            },
        }

        from_unit = cb_box1.get()
        to_unit = cb_box2.get()

        if from_unit == to_unit:
            lb2.config(text = lb1['text'])
        else:
            lb2.config(text = values[from_unit][to_unit])



frame1 = Frame(root, relief = 'solid', bd = 1)
frame2 = Frame(frame1)
frame3 = Frame(frame1)

lb1 = Label(frame2, text = 0)
lb1.pack(anchor = 'w')

list = ['Meters','Centimeters','Feet','Inches','Yards','Miles']
cb_box1 = ttk.Combobox(frame2, values = list, state = 'readonly')
cb_box1.pack()
cb_box1.set(list[0])

lb2 = Label(frame2, text = 0)
lb2.pack(anchor = 'w')

cb_box2 = ttk.Combobox(frame2, values = list, state = 'readonly')
cb_box2.pack()
cb_box2.set(list[3])

#button frame

button_texts = [['CE', '\u232B'], [7,8,9], [4,5,6], [1,2,3], [0, '.']]

row = 0
for r in button_texts:
    col = 1 if row in [0,4] else 0 
    for t in r:
        Mybutton(frame3, text = t, width = 8, height = 2).grid(row = row, column = col, padx =(2,2), pady = (2,2))
        col+=1
    row+=1

frame1.pack()
frame2.pack(anchor = 'w', padx = (20,20), pady = (20,0))
frame3.pack(padx = (20,20), pady = (0,20))
root.state('zoomed')
root.mainloop()