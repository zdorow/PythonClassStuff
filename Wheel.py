#######################################################################################
#
#     Program was written for the Advanced Programming class at Lakeland University
#     Author: Zachary Dorow
#     Teacher: Mr. Kevin Kurek
#     Last Edited: Nov 18, 2018
#
#     Description: The program function is to simulate a Slot Machine
#
#######################################################################################
import random


class Wheel:

    def __init__(self):
        self.pick = self.spin()

    def spin(self):
        random_pick = random.randint(1, 3)
        return random_pick


class Customer:

    def __init__(self, balance, bet):
        self.balance = self.set_balance(balance)
        self.bet = self.set_bet(bet)

    def set_balance(self, balance):
        if balance < 0:
            self.balance = 0
        elif balance > 1000:
            self.balance = 1000
        else:
            self.balance = balance
        return self.balance

    def get_balance(self):
        return self.balance

    def set_bet(self, bet):
        if bet in range(1, 4):
            self.bet = bet
        elif bet < 1:
            self.bet = 1
        else:
            self.bet = 4

        return self.bet

    def get_bet(self):
        return self.bet
