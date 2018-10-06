
users = []
questions = []
answers = []


class User(object):
    """docstring for creating User class"""
    def __init__(self, username, password, role="normal"):
        self.username = username
        self.password = password
        self.role = role

    def create_account(self):
        user = {"Username ": self.username,
        "Password ": self.password,
        "Role ": self.role}
        # print(user)
        users.append(user)

    def login(self):
        pass

    def get_questions(self):
        print(questions)

    def get_answers(self):
        print(answers)


class Normal(User):
    """docstring for Normal."""
    def __init__(self, username, password, role="normal"):
        super(Normal, self).__init__(username,password)
        # self.role = role

    # def post_question()
class Admin(User):
    """"""
    def __init__(self, username, password, role="admin"):
        super(Admin, self).__init__(username, password)
        
    def get_users(self):
        print(users)


class Question(object):
    """docstring for ."""
    def __init__(self, id, title, description, date):
        self.id = id
        self.title = title
        self.description = description
        self.date = date

    def post_question(self):
        question = {
        "Id ":self.id,
        "Title ":self.title,
        "Desc ":self.description,
        "Date ":self.date
        }
        # print(question)
        questions.append(question)

    def get_question(self, id):
        pass

class Answer(object):
    """docstring for ."""
    def __init__(self, ans_id,question_id, description, date):
        self.ans_id = ans_id
        self.question_id = question_id
        self.description = description
        self.date = date

    def post_answer(self):
        answer = {
        "Ans Id ":self.ans_id,
        "Quiz Id ":self.question_id,
        "Desc ":self.description,
        "Date ":self.date
        }
        # print(answer)
        answers.append(answer)


if __name__ == '__main__':

    # james = User("james@gmail.com", "12345")
    # james.create_account()

    tom = Normal("tom@gmail.com", "12345", "normal")
    tom.create_account()

    jim = Admin("jim@gmail.com", "12345", "admin")
    jim.create_account()
    jim.get_users()

    q1 = Question("1","How to","I was...","12.2.2018")
    q1.post_question()
    q2 = Question("2","How to","I was...","13.2.2018")
    q2.post_question()

    jim.get_questions()

    a1 = Answer("1","2","You can...","15.2.2018")
    a1.post_answer()

    a2 = Answer("2","1","This problem has...","14.2.2018")
    a2.post_answer()

    jim.get_answers()
