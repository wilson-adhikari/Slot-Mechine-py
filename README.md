# 🎰 Slot Machine Simulator (Python)

A simple slot machine simulation written in Python.  
It demonstrates object-oriented programming, randomness, and basic game logic in a clean and beginner-friendly way.

---

## 📌 Features

- Configurable number of reels  
- Customizable symbol set  
- Randomized spins using Python’s `random` module  
- Win detection when all reels match  
- Emoji-based output for readability and fun  

---

## 🧠 How It Works

- The slot machine consists of multiple reels.
- Each reel randomly selects a symbol when spun.
- A win occurs if **all reels show the same symbol**.
- The game runs in the terminal.

---

## 🧩 Code Overview

### `SlotMachine` Class

- `__init__(reels, symbols)`  
  Initializes the machine with a given number of reels and symbols.

- `spin()`  
  Randomly spins all reels and updates the machine state.

- `get_state()`  
  Returns the current symbols shown on the reels.

- `is_winner()`  
  Checks whether all reels match (winning condition).

---

## ▶️ Usage

### Requirements
- Python 3.x  
- No external libraries required

### Run the Program
```bash
python slot_machine.py
