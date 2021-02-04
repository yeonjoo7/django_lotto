from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

# Create your views here.
def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos':lottos})
    # 여기서는 dict를 context라고 부릅.

def hello(request):
    return HttpResponse('<h1 style="color:red;">Hello, world!</h1>')

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST) #filled form
        if form.is_valid():
            # 여기서 form.save()하면 바로 DB에 반영되지만 오류날 수 있어서 아래의 방법으로 실행
            lotto = form.save(commit = False)
            lotto.generate()
            return redirect('index_name')
    else:
        form = PostForm() #empty form
        return render(request, 'lotto/form.html', {'form':form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, 'lotto/detail.html', {'lotto':lotto})
