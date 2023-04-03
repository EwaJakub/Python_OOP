class SingleChoiceQuestion:
    def __init__(self, question, answer_list: list):
        self.question = question
        self.answer_list = answer_list

    def ask(self):
        print(self.question)
        num = 97
        for answer in self.answer_list:
            print(f"{chr(num)}) {answer}")
            num += 1
        choosen_answer = input("Wybierz odpowiedź a, b, c, ... , itp.:")
        while ord(choosen_answer) not in range(97, num):
            choosen_answer = input("Niepoprawna odpowiedź, spróbuj ponownie:")
        print("")
        return choosen_answer


class Questionnaire:
    def __init__(self, title):
        self.title = title
        self.question_list = []

    def add_question(self, question):
        self.question_list.append(question)
        return self.question_list

    def run(self):
        print(self.title)
        print("")
        question_dict = {}
        i = 0
        for que in self.question_list:
            answer = que.ask()
            question_dict[i] = answer
            i += 1
        print('Dziękuję!')
        return question_dict


questionnaire = Questionnaire('Ankieta dotycząca zadowolenia z wyboru laptopa')
q1 = SingleChoiceQuestion('Matryca', ['mniej niż 15 cali', 'od 15 do 17 cali', 'więcej niż 17 cali'])
q2 = SingleChoiceQuestion('Rodzaj ekranu', ['matowy', 'błyszczący'])
q3 = SingleChoiceQuestion('Czy polecisz go znajomemu?', ['zdecydowanie tak', 'raczej tak', 'nie mam zdania', 'raczej nie', 'zdecydowanie nie'])
questionnaire.add_question(q1)
questionnaire.add_question(q2)
questionnaire.add_question(q3)
answers = questionnaire.run()
print(answers)
