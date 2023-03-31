class QuizBrain:
    def __init__(self, question_list:list) -> None:
        self.score = 0
        self.question_number = 0
        self.question_list = question_list
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number} {current_question.text} (True/False)?: ")
        self.check_the_answer(users_answer = user_answer, correct_answer=current_question.answer)
        self.question_number += 1
        
    def still_has_questions(self) -> bool:
        num_of_questions = len(self.question_list)
        return self.question_number < num_of_questions
    
    def check_the_answer(self, users_answer, correct_answer):
        if users_answer.casefold() == correct_answer.casefold():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        self.show_score()
        
    def show_score(self):
        print(f"Your score is {self.score}/{self.question_number + 1}\n")
    