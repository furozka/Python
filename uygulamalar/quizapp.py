#quiz app
import random
class Question:
    
    def __init__(self, _text, _choices, _answer):
        self.text=_text
        self.coices=_choices
        self.answer=_answer
    
    def checkAnswer(self, _answer):
        return self.answer==_answer

q1 = Question("en iyi programlama dili hangisidir?",["python","c#","java","dart"],"python")
q2 = Question("en popüler programlama dili hangisidir?",["python","java","c#","dart"],"python")
q3 = Question("en çok kazandıran programlama dili hangisidir?",["python","java","dart","c#"],"python")

sorular = [q1,q2,q3]

print(q1.checkAnswer("java"))
print(q2.checkAnswer("python"))

class Quiz:

    def __init__(self, _questions):
        self.questions=random.sample(_questions,len(_questions))
        self.score=0
        self.questionIndex=0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        print(f"{self.questionIndex+1}. Soru: {self.getQuestion().text}")
        for i in self.getQuestion().coices:
            print("-"+i)
        cevap=input("Cevabınız: ")
        if cevap==self.getQuestion().answer:
            print("Doğru bildiniz")
            self.score+=1
        else:
            print(f"Yanlış cevap verdiniz doğrusu {self.getQuestion().answer}")
        self.questionIndex+=1
        Quiz.loadQuestion(self)
    
    def loadQuestion(self):
        if self.questionIndex<len(self.questions):
            print(f" Toplam {len(self.questions)} Sorudan {self.questionIndex+1}. Sorudasınız ".center(100,"*"))
            Quiz.displayQuestion(self)
        else:
            puan=100/len(self.questions)
            toplampuan=int(puan*self.score)
            print(f"Puanınız {toplampuan}")
        
    def displayScore(self):
        print("Sınav Sonucu".center(100,"*"))
        return f"Puanınız: {int(self.score*100/len(self.questions))} \nDoğru sayısı: {self.score}"

    def displayProgress(self):
        return f"{len(self.questions)} sorudan {self.questionIndex+1}. sorudasınız".center(100,"*")
    
    #def loadQuestion(self):


quiz=Quiz(sorular)
print(quiz.loadQuestion())
print(quiz.displayScore())