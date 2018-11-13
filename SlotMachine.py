#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Nov 18, 2018
#
#     Description: The program function is to simulate a Slot Machine
#
#
#######################################################################################
import re
import time
import random
import threading
from tkinter import *
from Wheel import *
from tkinter import simpledialog
from tkinter import messagebox


class slotMachineGUI:

    def __init__(self, master):

        lemon_img = PhotoImage(file=r"/Users/zach.dorow/IdeaProjects/barTab/lemon.png")
        grape_img = PhotoImage(file=r"/Users/zach.dorow/IdeaProjects/barTab/grape.png")
        cherry_img = PhotoImage(file=r"/Users/zach.dorow/IdeaProjects/barTab/cherry.png")

        pieces = {1: lemon_img, 2: grape_img, 3: cherry_img}

        # Getting the GUI going.
        self.master = master
        self.customer = Customer(0, 1)
        self.first_wheel = Wheel()
        self.second_wheel = Wheel()
        self.third_wheel = Wheel()

        master.title("Slot Machine")
        master.configure(background='black')

        top_frame = Frame(master, highlightbackground="green", highlightcolor="green", highlightthickness=1)
        self.top_frame = top_frame

        middle_frame = Frame(master, highlightbackground="green", highlightcolor="green", highlightthickness=2, bg="white",)
        self.middle_frame = middle_frame

        top_bottom_frame = Frame(master, highlightbackground="green", highlightcolor="green", highlightthickness=1)
        self.top_bottom_frame = top_bottom_frame

        middle_bottom_frame = Frame(master, highlightbackground="green", highlightcolor="green", highlightthickness=1)
        self.middle_bottom_frame = middle_bottom_frame

        bottom_bottom_frame = Frame(master, highlightbackground="green", highlightcolor="green", highlightthickness=1)
        self.bottom_bottom_frame = bottom_bottom_frame

        self.mainLabel = Label(top_frame, text="  Welcome to the Slot Machine!", fg="black", font="Helvetica 12 bold")
        self.balanceTotalOutput = Label(top_frame, text=f"Balance: 0",  fg="black", font="Helvetica 13 bold")
        self.betTotalOutput = Label(top_frame, text=f"Bet: 1", fg="black", font="Helvetica 13 bold")

        self.firstWheel = Label(middle_frame, image=lemon_img)
        self.firstWheel.image = lemon_img

        self.secondWheel = Label(middle_frame, image=grape_img)
        self.secondWheel.image = grape_img

        self.thirdWheel = Label(middle_frame, image=cherry_img)
        self.thirdWheel.image = cherry_img

        thread = threading.Thread(target=lambda: self.spin_the_wheels(pieces, self.first_wheel.pick, self.second_wheel.pick, self.third_wheel.pick), args=())
        self.thread = thread

        self.buttonToSpinWheels = Button(top_bottom_frame, text="   Spin    ", bg="white", fg="black", font="Helvetica 11 bold", command=lambda: self.thread_start_if_not(self.thread))
        self.buttonToAddFunds = Button(top_bottom_frame,   text=" Add Coins ", bg="white", fg="black",
                                       font="Helvetica 11 bold", command=lambda: self.add_coins(Customer.get_balance(self.customer)))

        self.buttonToIncreaseBet = Button(middle_bottom_frame, text=" Increase Bet ", bg="white", fg="black", font="Helvetica 10 bold", command=lambda: self.increase_bet(Customer.get_bet(self.customer)))
        self.buttonToDecreaseBet = Button(middle_bottom_frame, text=" Decrease Bet ", bg="white", fg="black", font="Helvetica 10 bold", command=lambda: self.decrease_bet(Customer.get_bet(self.customer)))
        self.buttonMaxBet = Button(middle_bottom_frame, text="\n Max Bet \n", bg="white", fg="black", font="Helvetica 10 bold", command=lambda: self.max_bet())

        self.buttonCashOut = Button(bottom_bottom_frame, text=" Cash Out ", bg="white", fg="black", font="Helvetica 10 bold", command=lambda: self.cash_out(Customer.get_balance(self.customer)))
        self.exitButton = Button(bottom_bottom_frame, text=" Exit ", command=master.destroy, bg="white", fg="blue", font="Helvetica 10 bold")

        self.top_frame.pack(padx=5, pady=2, fill="both", expand="yes")

        self.balanceTotalOutput.pack(side=LEFT, padx=7, pady=5)
        self.mainLabel.pack(side=LEFT, padx=7, pady=5)
        self.betTotalOutput.pack(side=LEFT, padx=7, pady=5)

        self.middle_frame.pack(padx=5, pady=5, fill="both", expand="yes")

        self.firstWheel.pack(side=LEFT, padx=5, pady=5)
        self.secondWheel.pack(side=LEFT, padx=5, pady=5)
        self.thirdWheel.pack(side=LEFT, padx=5, pady=5)

        self.top_bottom_frame.pack(padx=5, pady=2,  fill="both")

        self.buttonToAddFunds.pack(side=LEFT, padx=32, pady=5)
        self.buttonToSpinWheels.pack(side=RIGHT, padx=35, pady=5)

        self.middle_bottom_frame.pack(padx=5, pady=2,  fill="both")

        self.buttonToIncreaseBet.pack(side=LEFT, padx=25, pady=5)
        self.buttonMaxBet.pack(side=LEFT, padx=25, pady=5)
        self.buttonToDecreaseBet.pack(side=LEFT, padx=25, pady=5)

        self.bottom_bottom_frame.pack(padx=5, pady=2,  fill="both")

        self.buttonCashOut.pack(side=LEFT, padx=35, pady=5)
        self.exitButton.pack(side=RIGHT, padx=35, pady=5)

    def add_coins(self, customer_balance):

        added_coins = simpledialog.askinteger("Input", "How many coins would you like to add?", parent=self.master,
                                              minvalue=0, maxvalue=100)
        new_customer_balance = added_coins + customer_balance
        self.customer.set_balance(new_customer_balance)
        self.balanceTotalOutput.configure(text=f"Balance: {new_customer_balance}")

    def cash_out(self, customer_balance):
        messagebox.showinfo("Success", f"Printing Receipt... \n"
                            f"Please see the cashier for your payout of: {customer_balance}")
        self.customer.set_balance(0)
        self.balanceTotalOutput.configure(text="Balance: 0")

    def increase_bet(self, bet):
        new_current_bet = bet + 1
        self.customer.set_bet(new_current_bet)
        self.betTotalOutput.configure(text=f"Bet: {self.customer.get_bet()}")

    def decrease_bet(self, bet):
        new_current_bet = bet - 1
        self.customer.set_bet(new_current_bet)
        self.betTotalOutput.configure(text=f"Bet: {self.customer.get_bet()}")

    def max_bet(self):
        self.customer.set_bet(4)
        self.betTotalOutput.configure(text=f"Bet: {self.customer.get_bet()}")

    def spin_the_wheels(self, pieces, wheel_one, wheel_two, wheel_three):

        for run in range(1, 15):
            time.sleep(0.1)
            number, random_pick1 = random.choice(list(pieces.items()))
            number, random_pick2 = random.choice(list(pieces.items()))
            number, random_pick3 = random.choice(list(pieces.items()))
            self.firstWheel.configure(image=random_pick1)
            self.secondWheel.configure(image=random_pick2)
            self.thirdWheel.configure(image=random_pick3)

        new_thread = threading.Thread(target=lambda: self.spin_the_wheels(pieces, self.first_wheel.pick, self.second_wheel.pick, self.third_wheel.pick))
        self.new_thread = new_thread
        self.buttonToSpinWheels.configure(command=lambda: self.thread_start_if_not(self.new_thread))

        self.firstWheel.configure(image=pieces[wheel_one])
        self.secondWheel.configure(image=pieces[wheel_two])
        self.secondWheel.configure(image=pieces[wheel_three])

    def thread_start_if_not(self, thread):
            if not thread.is_alive():
                print(thread.is_alive())
                thread.start()


root = Tk()
slot_machine_gui = slotMachineGUI(root)
root.mainloop()
