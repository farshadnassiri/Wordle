import random

from utils import print_error, print_success, print_warning


class Wordle:
    def __init__(self,file_path,word_len = 5 ,limit = 1000):
        self.word_len=word_len
        self.file_path=file_path
        self.limit=limit
        self.words=self.generate_word_frequency()

    def generate_word_frequency(self):
        words_freq=[]
        with open(self.file_path) as f:
            for line in f:
                word,frequency=line.split(", ")
                frequency=int(frequency)
                word=word.strip().upper()
                words_freq.append((word,frequency))
        words_freq = list(filter(lambda w_freq :len(w_freq[0]) == self.word_len ,words_freq))
        words_freq = sorted(words_freq,key=lambda w_freq: w_freq[1],reverse=True)
        words_freq = words_freq[:self.limit]
        words=[word_freq[0] for word_freq in words_freq]
        return words

    def check_word(self, word, guess_word):
        for w_letter, g_letter in zip(word, guess_word):
            if w_letter == g_letter:
                print_success(f' {g_letter} ', end='')
                print(' ', end='')
            elif g_letter in word:
                print_warning(f' {g_letter} ', end='')
                print(' ', end='')
            else:
                print_error(f' {g_letter} ', end='')
                print(' ', end='')
        print()

    def run(self):
        word = random.choice(self.words)
        word=word.upper()

        num_try = 6
        success = False

        while num_try:
            guess_word = input(f'Enter a {self.word_len} letter word (or q to exit): ')
            if guess_word.lower() == "q":
                break
            guess_word=guess_word.upper()
            if len(guess_word) != self.word_len :
                print(f'Word must have {self.word_len} letters. You entered {len(guess_word)}!')
                continue
            self.check_word(word,guess_word)
            num_try -= 1
            if word == guess_word:
                print()
                print_success(' Congratulations! ')
                success = True
                break
        if not success:
            print_warning(f'Game over: The word was "{word}".')

        
