# Wordle (CLI) 🎮🧠

A simple command-line Wordle game written in Python. Guess the hidden 5-letter word in up to 6 tries. Colored feedback helps you narrow down the answer:

- 🟩 Green: Correct letter in the correct position
- 🟨 Yellow: Correct letter in the wrong position
- ⬛ Red: Letter not in the word

## Features ✨
- ✅ Uses a frequency-based word list to pick common words
- ✅ Clean colored output using `termcolor`
- ✅ Quit anytime with `q`
- ✅ Simple, readable code structure

## Requirements 🔧
- Python 3.8+
- `termcolor` package

Install dependency:

```bash
pip install termcolor
```

(Optional) Using a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\\Scripts\\activate
pip install termcolor
```

## How to Run ▶️
From the project root (this folder):

```bash
python src/data/run.py
```

You will be prompted to enter a 5-letter word each turn. Type `q` to exit.

## Gameplay 🕹️
- You have 6 attempts to guess the word.
- Input must be exactly 5 letters.
- After each guess, letters are color-coded:
  - Green = correct letter, correct place
  - Yellow = letter exists but in a different place
  - Red = letter not in the target word

## Configuration ⚙️
The game logic lives in `src/data/wordle.py`. Defaults:
- `word_len = 5`
- `limit = 1000` (top frequent words considered)
- Word list file: `src/data/words_frequency.txt` (format: `WORD, FREQUENCY`)

To change the word length or limit, update the `Wordle` constructor in `src/data/run.py` or modify defaults in `wordle.py`.

## Project Structure 🗂️
```text
src/
  data/
    run.py                # Entry point
    wordle.py             # Game logic
    utils.py              # Colored printing helpers
    words_frequency.txt   # Word, frequency dataset
```

## Troubleshooting 🧩
- "ModuleNotFoundError: No module named 'termcolor'": install it with `pip install termcolor`.
- Colors not showing correctly on some terminals: ensure your terminal supports ANSI colors.
- File path issues: run the script from the project root so relative paths to `src/data/words_frequency.txt` resolve correctly.

## License 📄
This project is for educational purposes. Feel free to use and modify.

Enjoy the game! 🎉
