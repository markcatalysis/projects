#hangman

class hangman(object):

    '''
    This object will request and accept a word that is composed of purely alphanumerics as a secret word and a new number for the number of tirals.
    '''

    def __init__(self):
        self.answer_raw=''
        self.answer=''
        self.trials=6
        self.letters_tried=[]
        self.reveal_list=[]
        self.current_trial=1
        self.keep_playing=True
        self.play_again=True
        self.current_letter=''
        self._win=False
        self.current_letter=''

    def clean_answer(self):
        self.answer=self.answer_raw.lower()
        # initiate reveal_list
        self.reveal_list=list('_'*len(self.answer))
        print (''.join(self.reveal_list))

    def new_letter(self):
        '''
        Input: None, but requests input.
        Output: None
        '''
        current_letter=raw_input('Guess a Letter: ')
        current_letter=current_letter.lower()
        if current_letter.isalpha() and len(current_letter)==1 and current_letter not in self.letters_tried:
            self.letters_tried.append(current_letter)
            self.letters_tried.sort()
            self.current_letter=current_letter
        else:
            print 'Letter Error. Try Again'
            self.new_letter()

    def process_letter(self):
        '''
        Checks if letter is in word and adds to fails
        '''
        if self.current_letter in list(self.answer):
            print('Nice...')
            for i,j in enumerate(list(self.answer)):
                if j==self.current_letter:
                    self.reveal_list[i]=self.current_letter
                    print ('Letters Found: %s' % ''.join(self.reveal_list), 'letters tried: %s' % self.letters_tried, 'attempts left: %s' % (self.trials-self.current_trial+1))
        else:
            self.current_trial+=1
            print('Letter Not in Word')
            print ('Letters Found: %s' % ''.join(self.reveal_list), 'letters tried: %s' % self.letters_tried, 'attempts left: %s' % (self.trials-self.current_trial+1))

    def start_hangman(self, attempts=6):
        solution=raw_input('Your Hangman Word Here: ')
        if type(solution)==str and solution.isalpha():
            change_tries=raw_input('Tries Set To = %s. Change? Input "y" or "True" to change: ' % self.trials)
            if change_tries=='y' or change_tries=='yes' or change_tries is True or change_tries == 'True':
                attempts=int(input('How Many Strikes/Bad-Tries Would You Like? Integer Smaller Than 26 Please: '))
                if type(attempts)==int and attempts<26 and attempts>0:
                    self.trials=attempts
                    self.answer_raw=solution
                else:
                    print('You goofed on your trial number pal. Sending you to top.')
                    self.start_hangman()
            elif change_tries.lower() in ['n', 'no', '', ' ']:
                self.answer_raw=solution
            else:
                print('You messed up. How did you mess this up? Oof. Think on it and try again. Sending you to top.')
                self.start_hangman()
        else:
            print('You messed up. Did your word have spaces letters or punctuation? Sorry Bud. Starting from the top.')
            self.start_hangman()

    def user_play_again(self):
        more_games=raw_input('Would you like to play again? y/n: ')
        if more_games in ['yes', 'y', 'True', True, 'y ', 'yes ']:
            self.letters_tried=[]
            self.reveal_list=[]
            self.current_trial=1
            self.keep_playing=True
            self.play_again=True
            self.current_letter=''
            self._win=False
            self.current_letter=''
            return True
        else:
            print('Thanks for playing!')
            return False

def play_hangman(new=True):
    if new==True:
        hm=hangman()
    keep_playing=True
    while keep_playing==True:
        hm.start_hangman()
        hm.clean_answer()
        while hm.current_trial<=hm.trials and hm._win==False:
            hm.new_letter()
            hm.process_letter()
            if '_' not in list(hm.reveal_list):
                hm._win=True
                print('You win!')
                keep_playing=hm.user_play_again()
                break
            elif hm.current_trial>hm.trials:
                print('You lose... Ouch!')
                print('Word was %s' %hm.answer)
                keep_playing=hm.user_play_again()
                break

if __name__=='__main__':

    play_hangman()
