class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        question = current_question.text
        answer = current_question.answer
        number = self.question_number

        user_guess = input(f'Q.{number}: {question} (True/False)?: ')
        self.check_answer(user_guess, answer)

    def check_answer(self, guess, answer):
        if guess.lower() == answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print("That's wrong.")

        print(f'The correct answer was {answer}')
        print(f'Your current score is {self.score}/{self.question_number}')
        print('\n')
