import random

class SlotMachine:
    def __init__(self, reels=3, symbols=None):
        if symbols is None:
            symbols = ['7️⃣', '👀', '🍳', '🙂', '⚠️']
        self.reels = reels
        self.symbols = symbols
        self.state = [random.choice(self.symbols) for _ in range(self.reels)]

    def spin(self):
        self.state = [random.choice(self.symbols) for _ in range(self.reels)]
        return self.state

    def get_state(self):
        return self.state

    def is_winner(self):
        return all(symbol == self.state[0] for symbol in self.state)
    
if __name__ == "__main__":
    slot_machine = SlotMachine()
    print("Initial State:", slot_machine.get_state())
    slot_machine.spin()
    print("Spun State:", slot_machine.get_state())
    if slot_machine.is_winner():
        print("Congratulations! You won!")
    else:
        print("Try again!")