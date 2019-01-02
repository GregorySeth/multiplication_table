from tkinter import Tk, Radiobutton, IntVar, Label
import random

class Multi:
    """Simple application for multiplying numbers """
    def __init__(self, window):
        self.window = window
        window.title("Multiplication")
        window.geometry("610x505")
        window.resizable(False, False)
        window.configure(background="light yellow")

        self.row_y = IntVar()
        self.row_x = IntVar()

        self.radio_y1 = Radiobutton(self.window, text="1", font=("Arial", 18, "bold"), variable=self.row_y, value=1, indicatoron=0, width=3, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_y2 = Radiobutton(self.window, text="2", font=("Arial", 18, "bold"), variable=self.row_y, value=2, indicatoron=0, width=3, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_y3 = Radiobutton(self.window, text="3", font=("Arial", 18, "bold"), variable=self.row_y, value=3, indicatoron=0, width=3, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_y4 = Radiobutton(self.window, text="4", font=("Arial", 18, "bold"), variable=self.row_y, value=4, indicatoron=0, width=3, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_y5 = Radiobutton(self.window, text="5", font=("Arial", 18, "bold"), variable=self.row_y, value=5, indicatoron=0, width=3, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_y6 = Radiobutton(self.window, text="6", font=("Arial", 18, "bold"), variable=self.row_y, value=6, indicatoron=0, width=3, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_y7 = Radiobutton(self.window, text="7", font=("Arial", 18, "bold"), variable=self.row_y, value=7, indicatoron=0, width=3, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_y8 = Radiobutton(self.window, text="8", font=("Arial", 18, "bold"), variable=self.row_y, value=8, indicatoron=0, width=3, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_y9 = Radiobutton(self.window, text="9", font=("Arial", 18, "bold"), variable=self.row_y, value=9, indicatoron=0, width=3, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_y0 = Radiobutton(self.window, text="10", font=("Arial", 18, "bold"), variable=self.row_y, value=10, indicatoron=0, width=3, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_x1 = Radiobutton(self.window, text="1", font=("Arial", 18, "bold"), variable=self.row_x, value=1, indicatoron=0, width=3, height=1, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_x2 = Radiobutton(self.window, text="2", font=("Arial", 18, "bold"), variable=self.row_x, value=2, indicatoron=0, width=3, height=1, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_x3 = Radiobutton(self.window, text="3", font=("Arial", 18, "bold"), variable=self.row_x, value=3, indicatoron=0, width=3, height=1, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_x4 = Radiobutton(self.window, text="4", font=("Arial", 18, "bold"), variable=self.row_x, value=4, indicatoron=0, width=3, height=1, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_x5 = Radiobutton(self.window, text="5", font=("Arial", 18, "bold"), variable=self.row_x, value=5, indicatoron=0, width=3, height=1, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_x6 = Radiobutton(self.window, text="6", font=("Arial", 18, "bold"), variable=self.row_x, value=6, indicatoron=0, width=3, height=1, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_x7 = Radiobutton(self.window, text="7", font=("Arial", 18, "bold"), variable=self.row_x, value=7, indicatoron=0, width=3, height=1, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_x8 = Radiobutton(self.window, text="8", font=("Arial", 18, "bold"), variable=self.row_x, value=8, indicatoron=0, width=3, height=1, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_x9 = Radiobutton(self.window, text="9", font=("Arial", 18, "bold"), variable=self.row_x, value=9, indicatoron=0, width=3, height=1, selectcolor="light green", background="light blue", command=self.operation)
        self.radio_x0 = Radiobutton(self.window, text="10", font=("Arial", 18, "bold"), variable=self.row_x, value=10, indicatoron=0, width=3, height=1, selectcolor="light green", background="light blue", command=self.operation)

        self.label_0 = Label(self.window, text="*", font=("Arial", 18, "bold"), background="light yellow")
        self.label_1 = Label(self.window, text="", font=("Arial", 60, "bold"), background="light yellow")

        # Arrangement
        self.radio_y1.grid(column=0, row=1, ipady=2)
        self.radio_y2.grid(column=0, row=2, ipady=2)
        self.radio_y3.grid(column=0, row=3, ipady=2)
        self.radio_y4.grid(column=0, row=4, ipady=2)
        self.radio_y5.grid(column=0, row=5, ipady=2)
        self.radio_y6.grid(column=0, row=6, ipady=2)
        self.radio_y7.grid(column=0, row=7, ipady=2)
        self.radio_y8.grid(column=0, row=8, ipady=2)
        self.radio_y9.grid(column=0, row=9, ipady=2)
        self.radio_y0.grid(column=0, row=10, ipady=2)
        self.radio_x1.grid(column=1, row=0)
        self.radio_x2.grid(column=2, row=0)
        self.radio_x3.grid(column=3, row=0)
        self.radio_x4.grid(column=4, row=0)
        self.radio_x5.grid(column=5, row=0)
        self.radio_x6.grid(column=6, row=0)
        self.radio_x7.grid(column=7, row=0)
        self.radio_x8.grid(column=8, row=0)
        self.radio_x9.grid(column=9, row=0)
        self.radio_x0.grid(column=10, row=0)
        self.label_1.grid(column=1, row=1, columnspan=9, rowspan=9)
        self.label_0.grid(column=0, row=0)

        # Radiobuttons with value = 1 selected by default
        self.radio_y1.invoke()
        self.radio_x1.invoke()

    # Multiplication function
    def operation(self):
        self.label_1["text"] = str(self.row_y.get() * self.row_x.get())
        # Differrent color per result
        self.label_1["foreground"] = random.choice(['dark slate gray', 'slate gray', 'midnight blue', 'navy', 'royal blue', 'dodger blue', 'forest green',
                      'dark green', 'steel blue', 'dark olive green', 'goldenrod', 'saddle brown',
                      'dark orange', 'orange red', 'red', 'deep pink', 'maroon', 'dark violet', 'blue violet', 'turquoise4',
                      'cyan4', 'brown4', 'IndianRed3', 'firebrick3', 'magenta4', 'red2', 'red3', 'red4'])


window = Tk()
multiplication_gui = Multi(window)
window.mainloop()
