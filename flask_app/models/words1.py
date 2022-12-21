from flask_app import app
from flask import Flask, redirect, render_template, request, session, flash
from flask_app.models.user import User
from flask_app.models.score import Score
import random



words = ['continue', 'bottle', 'guitar', 'chair', 'cement', 'stable', 'cabinet', 'telephone']

print(words)
print('i love my doggie')

def choose_word():
    chosen_word = random.choice(words)
    print(chosen_word)
    return chosen_word

# ---------this is from trying to display blanks before you guess-------------
    # displayed_word = session['displayed_word']
    # dw_with_spaces = displayed_word.replace('', ' ')[1: -1]

@app.route('/start-game')
def start_game():
    session['chosen_word'] = choose_word()
    session['letters_so_far'] = []
    session['guessed_letter'] = ''
    session['displayed_word'] = '_'
    x = len(session['chosen_word'])
    session['displayed_word'] = session['displayed_word'] * x
    if 'wrong_guesses' in session:
        session.pop('wrong_guesses')
    print(session['displayed_word'])
    return redirect('/guess-letter')


# -------this displays the blanks the first time, before you ever guess--------
# def first_display():
#     displayed_word = session['displayed_word']
#     dw_with_spaces = displayed_word.replace('', ' ')[1: -1]
#     return dw_with_spaces



def replace_blanks_w_letters(chosen_word, guessed_letter, displayed_word):
    for i in range(len(displayed_word)):
        if chosen_word[i] == guessed_letter:
            displayed_word = displayed_word[:i] + guessed_letter + displayed_word[i + 1:]
    return displayed_word








@app.route('/guess-letter', methods=['GET', 'POST'])
def handle_guess():

    message = ''
    displayed_word = None
    dw_with_spaces = ''
    if request.method == "POST":
        displayed_word = session['displayed_word']
        if 'guessed_letter' in request.form:
            guessed_letter = request.form['guessed_letter']
            print(guessed_letter)


# now testing to see if there are previous guesses
            if 'letters_so_far' in session:
                letters_so_far = session['letters_so_far']
                print(letters_so_far)
                session['letters_so_far'].append(guessed_letter)
                session.modified = True
# if letters_so_far isn't in session, it's your first guess
            else:
                session['letters_so_far'] = [guessed_letter]

# this is checking if the letter is in the word
            chosen_word = session['chosen_word']
            if guessed_letter in session['chosen_word']:
                displayed_word = replace_blanks_w_letters(chosen_word, guessed_letter, displayed_word)
                session['displayed_word'] = displayed_word
                dw_with_spaces = displayed_word.replace('', ' ')[1: -1]
                if '_' in dw_with_spaces:
                    message = f'good job, {guessed_letter} is in  {chosen_word}.'
                else:
                    message = 'congrats!! you won!!'
            else:
                displayed_word = replace_blanks_w_letters(chosen_word, guessed_letter, displayed_word)
                session['displayed_word'] = displayed_word
                dw_with_spaces = displayed_word.replace('', ' ')[1: -1]

                if 'wrong_guesses' not in session:
                    session['wrong_guesses'] = 0
                else: 
                    session['wrong_guesses'] += 1

                if session['wrong_guesses'] >= 5:
                    message = 'Game over buddy'
                else:
                    message = f'nope, sorry, {guessed_letter}  is not in  {chosen_word}.'
                print(message)
                print('wrong guesses:', session['wrong_guesses'])
            print(session['letters_so_far'])


    return render_template('dashboard.html', message = message, dw_with_spaces = dw_with_spaces)
