from django.shortcuts import render
# Create your views here.
def index(request):
    context = {
        'game_title': 'snake',
        'controls': 'Arrow keys or WASD',
        'rules': [
            'Eat the food to grow and score points',
            'Avoid hitting the walls or yourself',
        ],
    }
    return render(request,'game/index.html',context)