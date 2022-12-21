from flask_app import app
from flask_app.controllers import scores
from flask_app.controllers import users
from flask_app.controllers import words
from flask import Flask, redirect, render_template, request, session, flash
from flask_app.models.user import User
from flask_app.models.score import Score








# send back the changes in the word to the html each time
# send back the wrong letters to a letter bank on the html each time
# end the game when you either get too many wrong guesses or you get all the letters
# add the pictures everytime you get a word wrong







# make a function to clear some things from session at end of game-use pop session key (see counter assignment)






# words = ['continue', 'bottle', 'guitar', 'chair', 'cement', 'stable', 'cabinet', 'telephone']

# print(words)
# print('i love my doggie')

# def choose_word():
#     chosen_word = random.choice(words)
#     print(chosen_word)
#     return chosen_word

# chosen_word = choose_word()

# # print(chosen_word)


# @app.route('/guess-letter', methods=['POST'])
# def handle_guess():
#     data = {
#         'users_guess': request.form['users_guess']
#     } 
#     # if data in choose_word:
#     #     print('good job, that letter is in the word')
#     # else:
#     #     print('nope, sorry, that letter is not in the word')
#     print(data)
#     return redirect('/dashboard')
    
















if __name__ == '__main__':
    app.run(debug=True, port=5001)