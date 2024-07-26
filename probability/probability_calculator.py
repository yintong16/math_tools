from dataclasses import dataclass
import numpy as np


def EV_calculator(probabilities: list, values: list):
    """
    Calculates the expected value of a random variable given the probabilities of each value and the values themselves.
    :param probabilities: list of probabilities of each value
    :param values: list of values
    :return: expected value
    """
    return np.sum(np.multiply(probabilities, values))

def lottery_EV(total: int, prize_number: list, prize_value: list, ticket_price: int):
    '''
    total: total number of tickets
    prize_number: list of number of tickets that win each prize
    prize_value: list of value of each prize
    '''
    prize_value = [i-ticket_price for i in prize_value]
    prize_number.append(total - sum(prize_number))
    prize_value.append(-ticket_price)
    # print("prize_number: ", prize_number)
    # print("prize_value: ", prize_value)
    return EV_calculator([float(i)/total for i in prize_number], [prize_value])




@dataclass
class ScratchCard:
    name: str
    total: int
    prize_number: list
    prize_value: list
    ticket_price: int

def run():
    scratch_cards = [
        ScratchCard(name="彩虹宝石", total=5000000, prize_number=[1, 1, 90, 33000, 20000, 280000, 340000, 1060000], 
                    prize_value=[1000000, 10000, 1000, 500, 100, 50, 30, 20], ticket_price=20),

        ScratchCard(name="火辣辣", total=2000000, prize_number=[1, 10, 50, 1000, 2600, 32250, 10000, 40000, 164000, 360000],
                    prize_value=[300000, 5000, 500, 300, 200, 100, 50, 30, 20, 10], ticket_price=10),

        ScratchCard(name="出色", total=5000000, prize_number=[2, 2, 10, 500, 2000, 5000, 98000, 160000, 400000, 80000, 1200000],
                    prize_value=[1000000, 100000, 10000, 1000, 500, 200, 100, 50, 40, 30, 20], ticket_price=20),

        ScratchCard(name="大美四川", total=1000000, prize_number=[1, 4, 100, 800, 4000, 16000, 48000, 72000, 225000],
                    prize_value=[1000000, 10000, 1000, 500, 200, 100, 50, 30, 20], ticket_price=20),

        ScratchCard(name="海南·山水", total=1000000, prize_number=[1, 1, 10, 400, 2000, 3000, 44000, 40000, 340000],
                    prize_value=[1000000, 50000, 5000, 1000, 500, 100, 50, 30, 20], ticket_price=20),
        
        ScratchCard(name="唐风宋韵系列", total=2000000, prize_number=[1, 20, 1000, 1000, 4330, 100010, 100000, 140000, 400000],
                    prize_value=[1000000, 10000, 1000, 500, 300, 100, 60, 50, 30], ticket_price=30)
        
    ]
    for card in scratch_cards:
        print(f"Expected value of {card.name} is: {lottery_EV(card.total, card.prize_number, card.prize_value, card.ticket_price)}")

run()