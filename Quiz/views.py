from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *

from django.forms import formset_factory

# Create your views here.
def home(request):
    request.user
    if request.method == 'POST':
        print(request.POST)
        questions=QuesModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(request.POST.get(q.question2))
            print(request.POST.get(q.question3))
            print(request.POST.get(q.question4))
            print(request.POST.get(q.question5))
            print(request.POST.get(q.question6))
            print(request.POST.get(q.question7))
            print(q.ans)
            print(q.ans2)
            print(q.ans3)
            print(q.ans4)
            print(q.ans5)
            print(q.ans6)
            print(q.ans7)
            print()
            if q.ans ==  request.POST.get(q.question):    
                score+=10
                correct+=1
            else:
                wrong+=1
                
            if q.ans2 ==  request.POST.get(q.question2):    
                score+=10
                correct+=1
            else:
                wrong+=1
            if q.ans3 ==  request.POST.get(q.question3):    
                score+=10
                correct+=1
            else:
                wrong+=1
            if q.ans4 ==  request.POST.get(q.question4):    
                score+=10
                correct+=1
            else:
                wrong+=1
            if q.ans5 ==  request.POST.get(q.question5):    
                score+=10
                correct+=1
            else:
                wrong+=1
            if q.ans6 ==  request.POST.get(q.question6):    
                score+=10
                correct+=1
            else:
                wrong+=1
            if q.ans7 ==  request.POST.get(q.question7):    
                score+=10
                correct+=1
            else:
                wrong+=1
        
        # 여기에 랭킹과 나무를 띄워야함    
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total,
        }
        return render(request,'Quiz/result.html',context)
    
    else:
        questions=QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'Quiz/home.html',context)


    
# # 문제만들기
def addQuestion(request) :
    return render(request, 'Quiz/addQuestion.html')

def question(request):
    new_question = QuesModel()
    new_question.writer = request.user
    #new_question.op1 = request.POST['op1']
    #new_question.op2 = request.POST['op2']
    new_question.ans = request.POST['ans']
    new_question.question = request.POST['question']

    #new_question.op3 = request.POST['op3']
    #new_question.op4 = request.POST['op4']
    new_question.ans2 = request.POST['ans2']
    new_question.question2 = request.POST['question2']

    #new_question.op5 = request.POST['op5']
    #new_question.op6 = request.POST['op6']
    new_question.ans3 = request.POST['ans3']
    new_question.question3 = request.POST['question3']

    #new_question.op7 = request.POST['op7']
    #new_question.op8 = request.POST['op8']
    new_question.ans4 = request.POST['ans4']
    new_question.question4 = request.POST['question4']

    #new_question.op9 = request.POST['op9']
    #new_question.op10 = request.POST['op10']
    new_question.ans5 = request.POST['ans5']
    new_question.question5 = request.POST['question5']

    #new_question.op11 = request.POST['op11']
    #new_question.op12 = request.POST['op12']
    new_question.ans6 = request.POST['ans6']
    new_question.question6 = request.POST['question6']

    #new_question.op13 = request.POST['op13']
    #new_question.op14 = request.POST['op14']
    new_question.ans7 = request.POST['ans7']
    new_question.question7 = request.POST['question7']

    new_question.save()

    return redirect('home')





