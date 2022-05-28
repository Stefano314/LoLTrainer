import tkinter as tk
from tkinter import ttk
import sv_ttk
from PIL import ImageTk, Image

class App(ttk.Frame):
    def __init__(self, parents, items):
        ttk.Frame.__init__(self)

        # Images
        self.img_1 = ImageTk.PhotoImage(items[0].item_image(png = True).resize((60, 60)))
        self.img_name_1 = items[0].name
        self.img_2 = ImageTk.PhotoImage(items[1].item_image(png = True).resize((60, 60)))
        self.img_name_2 = items[1].name
        self.img_3 = ImageTk.PhotoImage(items[2].item_image(png = True).resize((60, 60)))
        self.img_name_3 = items[2].name
        self.img_4 = ImageTk.PhotoImage(items[3].item_image(png = True).resize((60, 60)))
        self.img_name_4 = items[3].name
        self.img_5 = ImageTk.PhotoImage(items[4].item_image(png = True).resize((60, 60)))
        self.img_name_5 = items[4].name
        self.img_6 = ImageTk.PhotoImage(items[5].item_image(png = True).resize((60, 60)))
        self.img_name_6 = items[5].name

        # Null variable
        self.empty_spot = tk.StringVar(value=" ")

        # Make the app layout

        # for ind in range(21):
        #     self.rowconfigure(index = ind, weight = 1)
        #     self.columnconfigure(index = ind, weight = 1)


    #
    #     self.result = tk.StringVar(value = "")
    #
    #     # Create widgets
        self.setup_widgets(items)

    def show_item_stats(self, item):
        root = tk.Tk()
        root.title(f"{item.name}")
        root.geometry("400x200")
        root.attributes("-topmost", True)  # It stays always on top of other windows


        root.update()
        root.minsize(root.winfo_width(), root.winfo_height())
        x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
        y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
        root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

        frame = ttk.Frame(root)

        canvas = tk.Canvas(frame)
        scrollbar = ttk.Scrollbar(frame, orient = "vertical", command = canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion = canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window = scrollable_frame, anchor = "nw")
        canvas.configure(yscrollcommand = scrollbar.set)

        gold = ttk.Label(scrollable_frame, text = f"  Gold {item.gold}  ", font = 'Calibri 20', borderwidth = 2, relief = 'solid' )
        gold.grid(row = 0, column = 0, columnspan = 1, padx = 10, pady = 4, sticky = "ew")
        ad = ttk.Label(scrollable_frame, text = f"  AD {item.gold}  ", font = 'Calibri 20', borderwidth = 2, relief = 'solid')
        ad.grid(row = 1, column = 0, columnspan = 1, padx = 10, pady = 4, sticky = "ew")
        ap = ttk.Label(scrollable_frame, text = f"  AP {item.AP}  ", font = 'Calibri 20', borderwidth = 2, relief = 'solid')
        ap.grid(row = 2, column = 0, columnspan = 1, padx = 10, pady = 4, sticky = "ew")
        hp = ttk.Label(scrollable_frame, text = f"  HP {item.HP}  ", font = 'Calibri 20', borderwidth = 2, relief = 'solid')
        hp.grid(row = 3, column = 0, columnspan = 1, padx = 10, pady = 4, sticky = "ew")
        p_a = ttk.Label(scrollable_frame, text = f"  Physical Armor {item.Ph_armor}  ", font = 'Calibri 20', borderwidth = 2, relief = 'solid')
        p_a.grid(row = 4, column = 0, columnspan = 1, padx = 10, pady = 4, sticky = "ew")
        m_a = ttk.Label(scrollable_frame, text = f"  Magical Armor {item.Ma_armor}  ", font = 'Calibri 20', borderwidth = 2, relief = 'solid')
        m_a.grid(row = 5, column = 0, columnspan = 1, padx = 10, pady = 4, sticky = "ew")

        frame.pack()
        canvas.pack(side = "left", fill = "both", expand = True)
        scrollbar.pack(side = "right", fill = "y")


    def setup_widgets(self, items):


        # Create a Frame for input widgets
        # self.widgets_frame = ttk.LabelFrame(self, text="Checkbuttons", padding=(20, 10))#ttk.Frame(self, padding = (0, 0, 0,20))
        # self.widgets_frame.grid(
        #     row = 0, column = 0, padx = (20, 10), pady = (20, 10), sticky = "nsew"
        # )
        # self.widgets_frame.grid(
        #     row = 0, column = 0, padx = 10, pady = (30, 10), sticky = "nsew", rowspan = 3
        # )
        # self.widgets_frame.columnconfigure(index = 0, weight = 1)
        #
        # self.label = ttk.Label(self, text = " ITEMS HOLD ", font = 'Calibri 20', borderwidth = 2, relief="solid")\
        #     .grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 10, sticky = "nw")


        # # OptionMenu
        # self.optionmenu = ttk.OptionMenu(
        #     self.widgets_frame, self.empty_spot, " ", *self.items_hold
        # )
        # self.optionmenu.grid(row = 6, column = 0, padx = 6, pady = 10, sticky = "nsew")

        # Img Pics
        self.img1 = ttk.Button(self, image = self.img_1, command = lambda: self.show_item_stats(items[0]))
        self.img1.grid(row = 2, column = 0, columnspan = 1, padx = 10, pady = 4, sticky = "nw")
        # self.img1.configure(self.)
        self.img2 = ttk.Button(self, image = self.img_2, command = lambda: self.show_item_stats(items[1]))
        self.img2.grid(row = 2 , column = 1, columnspan = 1, padx = 10, pady = 4, sticky = "nw")

        self.img3 = ttk.Button(self, image = self.img_3, command = lambda: self.show_item_stats(items[2]))
        self.img3.grid(row = 2, column = 2, columnspan = 1, padx = 10, pady = 4, sticky = "nw")

        self.img4 = ttk.Button(self, image = self.img_4, command = lambda: self.show_item_stats(items[3]))
        self.img4.grid(row = 3, column = 0, columnspan = 1, padx = 10, pady = 4, sticky = "nw")

        self.img5 = ttk.Button(self, image = self.img_5, command = lambda: self.show_item_stats(items[4]))
        self.img5.grid(row = 3, column = 1, columnspan = 1, padx = 10, pady = 4, sticky = "nw")

        self.img6 = ttk.Button(self, image = self.img_6, command = lambda: self.show_item_stats(items[5]))
        self.img6.grid(row = 3, column = 2, columnspan = 1, padx = 10, pady = 4, sticky = "nw")


        # canvas = tk.Canvas(root, width = 40, height = 40)
        # canvas.pack()
        # pilImage = item.item_image(png=True)
        # image = ImageTk.PhotoImage(pilImage)
        # imagesprite = canvas.create_image(40, 40, image = image)
        # ttk.Label(self, image=image).grid(row = 2, column = 1)

    #
        # for index, key in enumerate("147C2580369=+-*/"):
        #     ttk.Button(
        #         self,
        #         text = key,
        #         style = "Accent.TButton" if key == "=" else "TButton",
        #         #command = partial(self.button_pressed, key),
        #     ).grid(row = index % 4 + 1, column = index // 4, sticky = "nsew", padx = 2, pady = 2)
    #
    # def button_pressed(self, key):
    #     if key == "C":
    #         self.result.set("")
    #     elif key == "=":
    #         self.result.set(str(round(eval(self.result.get()))))
    #     else:
    #         self.result.set(self.result.get() + key)