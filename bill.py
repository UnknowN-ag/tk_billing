from tkinter import *
import math, random
from tkinter import messagebox

class BillApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color = "#074463"
        title = Label(self.root, text = "Billing Software", bd = 12, relief = GROOVE, bg = bg_color, fg = "white", font = ("times new roman", 30, "bold"), pady=5)
        title.pack(fill = X)
        #=================variables=====================
        self.bath_soap = DoubleVar()
        self.face_cream = DoubleVar()
        self.face_wash = DoubleVar()
        self.shampoo = DoubleVar()
        self.hair_gel = DoubleVar()
        self.body_lotion = DoubleVar()

        self.rice = DoubleVar()
        self.olive_oil = DoubleVar()
        self.wheat = DoubleVar()
        self.sugar = DoubleVar()
        self.tea = DoubleVar()
        self.dal = DoubleVar()

        self.pepsi = DoubleVar()
        self.coke = DoubleVar()
        self.frooti = DoubleVar()
        self.sprite = DoubleVar()
        self.appy = DoubleVar()
        self.maza = DoubleVar()

        self.cos_price = StringVar()
        self.gro_price = StringVar()
        self.drink_price = StringVar()

        self.cos_tax = StringVar()
        self.gro_tax = StringVar()
        self.drink_tax = StringVar()

        self.c_name = StringVar()
        self.c_mobile = StringVar()
        self.c_bill_no = StringVar()
        rand_num = random.randint(1000,9999)
        self.c_bill_no.set(str(rand_num))

        self.search_bill = StringVar()

        

        #=============customer details=============
        F1 = LabelFrame(self.root, text= "Customers Details :", bd = 10, relief = GROOVE, font = ("times new roman", 15, "bold"), bg = bg_color, fg = "gold")
        F1.place(x = 0, y = 80, relwidth = 1)
            #================cname===========================
        cname_lbl = Label(F1, text = "Customer Name:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "white")
        cname_lbl.grid(row = 0, column = 0, padx = 40, pady = 5)

        cname_input = Entry(F1,textvariable = self.c_name, width = 18, font = "arial 12", bd = 5, relief = SUNKEN)
        cname_input.grid(row = 0, column = 1, pady = 5, padx = 10)
            #===============cmobile===========================
        cmobile_lbl = Label(F1, text = "Phone No.:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "white")
        cmobile_lbl.grid(row = 0, column = 2, padx = 30, pady = 5)

        cmobile_input = Entry(F1,textvariable = self.c_mobile, width = 18, font = "arial 12", bd = 5, relief = SUNKEN)
        cmobile_input.grid(row = 0, column = 3, pady = 5, padx = 10)
            #===============cbill===========================
        cbill_lbl = Label(F1, text = "Bill Number:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "white")
        cbill_lbl.grid(row = 0, column = 4, padx = 30, pady = 5)

        cbill_input = Entry(F1, textvariable = self.search_bill, width = 18, font = "arial 12", bd = 5, relief = SUNKEN)
        cbill_input.grid(row = 0, column = 5, pady = 5, padx = 10)

        search_btn = Button(F1, text = "Search", font = "arial 10 bold", width = 10)
        search_btn.grid(row = 0, column = 6, padx = 10, pady = 10)

        #=============Cosmetics Frame=============
        F2 = LabelFrame(self.root, text= "Cosmetics :", bd = 10, relief = GROOVE, font = ("times new roman", 15, "bold"), bg = bg_color, fg = "gold")
        F2.place( y = 165, width = 335, height = 350)

        bath_lbl = Label(F2, text = "Bath Soap:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        bath_lbl.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "w")
        bath_input = Entry(F2,textvariable = self.bath_soap, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        bath_input.grid(row = 0, column = 1, pady = 10, padx = 3)

        face_cream_lbl = Label(F2, text = "Face Cream:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        face_cream_lbl.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
        face_cream_input = Entry(F2,textvariable = self.face_cream, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        face_cream_input.grid(row = 1, column = 1, pady = 10, padx = 3)

        face_wash_lbl = Label(F2, text = "Face Wash:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        face_wash_lbl.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "w")
        face_wash_input = Entry(F2,textvariable = self.face_wash, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        face_wash_input.grid(row = 2, column = 1, pady = 10, padx = 3)

        hair_shampoo_lbl = Label(F2, text = "Shampoo:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        hair_shampoo_lbl.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "w")
        hair_shampoo_input = Entry(F2,textvariable = self.shampoo, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        hair_shampoo_input.grid(row = 3, column = 1, pady = 10, padx = 3)

        hair_gel_lbl = Label(F2, text = "Hair Gel:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        hair_gel_lbl.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "w")
        hair_gel_input = Entry(F2,textvariable = self.hair_gel, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        hair_gel_input.grid(row = 4, column = 1, pady = 10, padx = 3)

        body_lotion_lbl = Label(F2, text = "Body Lotion:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        body_lotion_lbl.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "w")
        body_lotion_input = Entry(F2,textvariable = self.body_lotion, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        body_lotion_input.grid(row = 5, column = 1, pady = 10, padx = 3)

        #=============Grocery Frame=============
        F3 = LabelFrame(self.root, text= "Grocery :", bd = 10, relief = GROOVE, font = ("times new roman", 15, "bold"), bg = bg_color, fg = "gold")
        F3.place(x = 337, y = 165, width = 300, height = 350)

        rice_lbl = Label(F3, text = "Rice:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        rice_lbl.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "w")
        rice_input = Entry(F3,textvariable = self.rice, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        rice_input.grid(row = 0, column = 1, pady = 10, padx = 3)

        oil_lbl = Label(F3, text = "Olive Oil:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        oil_lbl.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
        oil_input = Entry(F3,textvariable = self.olive_oil, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        oil_input.grid(row = 1, column = 1, pady = 10, padx = 3)

        Wheat_lbl = Label(F3, text = "Wheat:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        Wheat_lbl.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "w")
        Wheat_input = Entry(F3,textvariable = self.wheat, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        Wheat_input.grid(row = 2, column = 1, pady = 10, padx = 3)

        sugar_lbl = Label(F3, text = "Sugar:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        sugar_lbl.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "w")
        sugar_input = Entry(F3,textvariable = self.sugar, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        sugar_input.grid(row = 3, column = 1, pady = 10, padx = 3)

        tea_lbl = Label(F3, text = "Tea:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        tea_lbl.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "w")
        tea_input = Entry(F3,textvariable = self.tea, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        tea_input.grid(row = 4, column = 1, pady = 10, padx = 3)

        dal_lbl = Label(F3, text = "Dal:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        dal_lbl.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "w")
        dal_input = Entry(F3,textvariable = self.dal, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        dal_input.grid(row = 5, column = 1, pady = 10, padx = 3)

        #=============Cold Drink Frame=============
        F4 = LabelFrame(self.root, text= "Cold Drinks :", bd = 10, relief = GROOVE, font = ("times new roman", 15, "bold"), bg = bg_color, fg = "gold")
        F4.place(x = 640, y = 165, width = 300, height = 350)

        pepsi_lbl = Label(F4, text = "Pepsi:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        pepsi_lbl.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "w")
        pepsi_input = Entry(F4,textvariable = self.pepsi, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        pepsi_input.grid(row = 0, column = 1, pady = 10, padx = 3)

        coke_lbl = Label(F4, text = "Coke:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        coke_lbl.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")
        coke_input = Entry(F4,textvariable = self.coke, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        coke_input.grid(row = 1, column = 1, pady = 10, padx = 3)

        frooti_lbl = Label(F4, text = "Frooti:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        frooti_lbl.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "w")
        frooti_input = Entry(F4,textvariable = self.frooti, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        frooti_input.grid(row = 2, column = 1, pady = 10, padx = 3)

        sprite_lbl = Label(F4, text = "Sprite:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        sprite_lbl.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "w")
        sprite_input = Entry(F4,textvariable = self.sprite, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        sprite_input.grid(row = 3, column = 1, pady = 10, padx = 3)

        appy_lbl = Label(F4, text = "Appy:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        appy_lbl.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "w")
        appy_input = Entry(F4,textvariable = self.appy, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        appy_input.grid(row = 4, column = 1, pady = 10, padx = 3)

        maza_lbl = Label(F4, text = "Maza:", font = ("times new roman", 15, "bold"), bg = bg_color, fg = "lightgreen")
        maza_lbl.grid(row = 5, column = 0, padx = 10, pady = 10, sticky = "w")
        maza_input = Entry(F4,textvariable = self.maza, width = 15, font = "arial 12", bd = 5, relief = SUNKEN)
        maza_input.grid(row = 5, column = 1, pady = 10, padx = 3)

        #=============Bill Frame=============
        F5 = Frame(self.root,  bd = 10, relief = GROOVE)
        F5.place(x = 945, y = 165, width = 384, height = 350)
        bill_title = Label(F5, text = "Bill Area", font = ("times new roman", 15, "bold"), bd = 7, relief = GROOVE)
        bill_title.pack(fill = X)
        scroll_y = Scrollbar(F5, orient = VERTICAL)
        scroll_y.pack(side = RIGHT, fill = Y)
        self.txtarea = Text(F5, yscrollcommand = scroll_y.set)
        self.txtarea.pack(fill = BOTH, expand = 1)
        scroll_y.config(command = self.txtarea.yview)

        #==========Button Frame=============
        F6 = LabelFrame(self.root, text = "Bill Menu", font = ("times new roman", 15, "bold"), fg = "gold", bg = bg_color, bd = 7, relief = GROOVE)
        F6.place(y = 517,relwidth = 1, height = 180)

        tot_cos_lbl = Label(F6, text = "Total Cosmetic Price:", font = ("times new roman", 13, "bold"), bg = bg_color, fg = "white")
        tot_cos_lbl.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "w")
        tot_cos_input = Entry(F6,textvariable = self.cos_price, width = 12, font = "arial 12", bd = 5, relief = SUNKEN)
        tot_cos_input.grid(row = 0, column = 1, pady = 8, padx = 3)

        tot_gro_lbl = Label(F6, text = "Total Grocery Price:", font = ("times new roman", 13, "bold"), bg = bg_color, fg = "white")
        tot_gro_lbl.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = "w")
        tot_gro_input = Entry(F6,textvariable = self.gro_price, width = 12, font = "arial 12", bd = 5, relief = SUNKEN)
        tot_gro_input.grid(row = 1, column = 1, pady = 8, padx = 3)

        tot_drinks_lbl = Label(F6, text = "Total Drinks Price:", font = ("times new roman", 13, "bold"), bg = bg_color, fg = "white")
        tot_drinks_lbl.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
        tot_drinks_input = Entry(F6,textvariable = self.drink_price, width = 12, font = "arial 12", bd = 5, relief = SUNKEN)
        tot_drinks_input.grid(row = 2, column = 1, pady = 8, padx = 3)


        tot_cos_tax_lbl = Label(F6, text = "Total Cosmetic Tax:", font = ("times new roman", 13, "bold"), bg = bg_color, fg = "white")
        tot_cos_tax_lbl.grid(row = 0, column = 2, padx = 8, pady = 5, sticky = "w")
        tot_cos_tax_input = Entry(F6,textvariable = self.cos_tax, width = 12, font = "arial 12", bd = 5, relief = SUNKEN)
        tot_cos_tax_input.grid(row = 0, column = 3, pady = 8, padx = 3)

        tot_gro_tax_lbl = Label(F6, text = "Total Grocery Tax:", font = ("times new roman", 13, "bold"), bg = bg_color, fg = "white")
        tot_gro_tax_lbl.grid(row = 1, column = 2, padx = 8, pady = 5, sticky = "w")
        tot_gro_tax_input = Entry(F6,textvariable = self.gro_tax, width = 12, font = "arial 12", bd = 5, relief = SUNKEN)
        tot_gro_tax_input.grid(row = 1, column = 3, pady = 8, padx = 3)

        tot_drinks_tax_lbl = Label(F6, text = "Total Drinks Tax:", font = ("times new roman", 13, "bold"), bg = bg_color, fg = "white")
        tot_drinks_tax_lbl.grid(row = 2, column = 2, padx = 8, pady = 5, sticky = "w")
        tot_drinks_tax_input = Entry(F6,textvariable = self.drink_tax, width = 12, font = "arial 12", bd = 5, relief = SUNKEN)
        tot_drinks_tax_input.grid(row = 2, column = 3, pady = 8, padx = 3)

        btn_frame = Frame(F6, bd = 7, relief = GROOVE)
        btn_frame.place(x = 630, width = 680, height = 140)

        total_btn = Button(btn_frame,command = self.total, text = "Total", font =("arial", 15, "bold"), bg = "cadetblue", fg = "white", width = 10, bd = 5, pady = 15)
        total_btn.grid(row = 0, column = 0, pady = 20, padx = 10)

        generate_btn = Button(btn_frame,command =self.bill_area, text = "Generate Bill", font =("arial", 15, "bold"), bg = "cadetblue", fg = "white", width = 13, bd = 5, pady = 15)
        generate_btn.grid(row = 0, column = 2, pady = 20, padx = 10)

        clear_btn = Button(btn_frame, text = "Clear", font =("arial", 15, "bold"), bg = "cadetblue", fg = "white", width = 10, bd = 5, pady = 15)
        clear_btn.grid(row = 0, column = 3, pady = 20, padx = 10)

        exit_btn = Button(btn_frame, text = "Exit", font =("arial", 15, "bold"), bg = "cadetblue", fg = "white", width = 10, bd = 5, pady = 15)
        exit_btn.grid(row = 0, column = 4, pady = 20, padx = 10)

        self.welcome_bill()

    def total(self):
        self.tot_bath_soap_price = (self.bath_soap.get()*20)
        self.tot_face_cream_price = (self.face_cream.get()*40)
        self.tot_face_wash_price = (self.face_wash.get()*35)
        self.tot_shampoo_price = (self.shampoo.get()*50)
        self.tot_hair_gel_price = (self.hair_gel.get()*15)
        self.tot_body_lotion_price = (self.body_lotion.get()*25) 
        self.total_cos_price =float(
            self.tot_bath_soap_price +
            self.tot_face_cream_price +
            self.tot_face_wash_price +
            self.tot_shampoo_price +
            self.tot_hair_gel_price +
            self.tot_body_lotion_price)
        self.cos_price.set(str(self.total_cos_price))
        self.cos_tax.set(str(round(self.total_cos_price*0.18, 2)))
        #========================================================================
        self.tot_rice_price = (self.rice.get()*45)
        self.tot_wheat_price = (self.wheat.get()*20)
        self.tot_olive_oil_price = (self.olive_oil.get()*180)
        self.tot_sugar_price = (self.sugar.get()*40)
        self.tot_tea_price = (self.tea.get()*100)
        self.tot_dal_price = (self.dal.get()*70)
        self.total_gro_price =float(
            self.tot_rice_price +
            self.tot_olive_oil_price +
            self.tot_wheat_price +
            self.tot_sugar_price +
            self.tot_tea_price +
            self.tot_dal_price)
        self.gro_price.set(str(self.total_gro_price))
        self.gro_tax.set(str(round(self.total_gro_price*0.18, 2)))
        #========================================================================
        self.tot_pepsi_price = (self.pepsi.get()*20)
        self.tot_coke_price = (self.coke.get()*20)
        self.tot_frooti_price = (self.frooti.get()*30)
        self.tot_sprite_price = (self.sprite.get()*25)
        self.tot_appy_price = (self.appy.get()*10)
        self.tot_maza_price = (self.maza.get()*25)
        self.total_drink_price =float(
            self.tot_pepsi_price +
            self.tot_coke_price +
            self.tot_frooti_price +
            self.tot_sprite_price +
            self.tot_appy_price +
            self.tot_maza_price)
        self.drink_price.set(str(self.total_drink_price))
        self.drink_tax.set(str(round(self.total_drink_price*0.18, 2)))

        self.total_price = (
            self.total_cos_price +
            self.total_gro_price +
            self.total_drink_price +
            float(self.cos_tax.get()) +
            float(self.gro_tax.get()) +
            float(self.drink_tax.get())
        )

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END, "\tWelcome Retail Shop\n")
        self.txtarea.insert(END, f"\nBill Number : {self.c_bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\nContact : {self.c_mobile.get()}")
        self.txtarea.insert(END, f"\n==========================================")
        self.txtarea.insert(END, f"\nProducts\t\tQty\t\tPrice")
        self.txtarea.insert(END, f"\n==========================================")

    def bill_area(self):
        if self.c_name.get() == "" or self.c_mobile.get() == "":
            messagebox.showerror("Error","Customer details are must")
        elif self.cos_price.get() == "0.0" and self.gro_tax.get() == "0.0" and self.drink_tax.get() == "0.0":
            messagebox.showerror("Error","No products are selected")
        else:
            self.welcome_bill()
            #================cos==================
            if self.bath_soap.get()!=0:
                self.txtarea.insert(END,f"\nBath Soap\t\t{self.bath_soap.get()}\t\t{self.tot_bath_soap_price}")
            if self.face_cream.get()!=0:
                self.txtarea.insert(END,f"\nFace Cream\t\t{self.face_cream.get()}\t\t{self.tot_face_cream_price}")
            if self.face_wash.get()!=0:
                self.txtarea.insert(END,f"\nFace Wash\t\t{self.face_wash.get()}\t\t{self.tot_face_wash_price}")
            if self.shampoo.get()!=0:
                self.txtarea.insert(END,f"\nShampoo\t\t{self.shampoo.get()}\t\t{self.tot_shampoo_price}")
            if self.hair_gel.get()!=0:
                self.txtarea.insert(END,f"\nHair Gel\t\t{self.hair_gel.get()}\t\t{self.tot_hair_gel_price}")
            if self.body_lotion.get()!=0:
                self.txtarea.insert(END,f"\nBody Lotion\t\t{self.body_lotion.get()}\t\t{self.tot_body_lotion_price}")

            #================gro==================
            if self.rice.get()!=0.0:
                self.txtarea.insert(END,f"\nRice\t\t{self.rice.get()}\t\t{self.tot_rice_price}")
            if self.olive_oil.get()!=0:
                self.txtarea.insert(END,f"\nOlive Oil\t\t{self.olive_oil.get()}\t\t{self.tot_olive_oil_price}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\nWheat\t\t{self.wheat.get()}\t\t{self.tot_wheat_price}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\nSugar\t\t{self.sugar.get()}\t\t{self.tot_sugar_price}")
            if self.tea.get()!=0:
                self.txtarea.insert(END,f"\nTea\t\t{self.tea.get()}\t\t{self.tot_tea_price}")
            if self.dal.get()!=0:
                self.txtarea.insert(END,f"\nDal\t\t{self.dal.get()}\t\t{self.tot_dal_price}")

            #================drinks==================
            if self.pepsi.get()!=0.0:
                self.txtarea.insert(END,f"\nPepsi\t\t{self.pepsi.get()}\t\t{self.tot_pepsi_price}")
            if self.coke.get()!=0:
                self.txtarea.insert(END,f"\nCoke\t\t{self.coke.get()}\t\t{self.tot_coke_price}")
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\nFrooti\t\t{self.frooti.get()}\t\t{self.tot_frooti_price}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\nSprite\t\t{self.sprite.get()}\t\t{self.tot_sprite_price}")
            if self.appy.get()!=0:
                self.txtarea.insert(END,f"\nAppy\t\t{self.appy.get()}\t\t{self.tot_appy_price}")
            if self.maza.get()!=0:
                self.txtarea.insert(END,f"\nMaza\t\t{self.maza.get()}\t\t{self.tot_maza_price}")

            self.txtarea.insert(END, f"\n------------------------------------------")
            if (self.cos_tax.get() != "0.0") and (self.cos_tax.get() != ""):
                self.txtarea.insert(END, f"\nCosmetic Tax\t\t\t\t{self.cos_tax.get()}")
            if (self.gro_tax.get() != "0.0") and (self.cos_tax.get() != ""):
                self.txtarea.insert(END, f"\nGrocery Tax\t\t\t\t{self.gro_tax.get()}")
            if (self.drink_tax.get() != "0.0") and (self.cos_tax.get() != ""):
                self.txtarea.insert(END, f"\nDrink Tax\t\t\t\t{self.drink_tax.get()}")
            self.txtarea.insert(END, f"\nTotal Bill\t\t\t\t{round(self.total_price,2)}")
            self.txtarea.insert(END, f"\n------------------------------------------")



root = Tk()
obj = BillApp(root)
root.mainloop()