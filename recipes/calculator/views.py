from django.shortcuts import render, reverse
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    # можете добавить свои рецепты ;)
    },
    'hod_dog': {
        'булка, шт': 1,
        'сосиська, шт': 1,
        'горчица, г': 10,
    },
    'mack_chicken': {
        'булочка, ломтик': 2,
        'куринное филе, ломтик': 1,
        'сыр, ломтик': 1,
        'лук, ломтик': 1,
        'салат, лист': 1,
    },
}


def home(request):
    msg = ""
    for i in DATA.keys():
        msg += f"<a href= {reverse(i)}>{i}</a><br>"
    return HttpResponse(f"{msg}")


def buter(request):
    # count = int(request.GET.get("servings", 1))   * count,
    context = {
      'recipe': {
         'хлеб, ломтик': 1,
         'колбаса, ломтик': 1,
         'сыр, ломтик': 1,
         'помидор, ломтик': 1,
      }
    }
    return render(request, 'calculator/index.html', context)


def omlet(request):
    # count = int(request.GET.get("servings", 1))
    context = {
        'recipe': {
            'яйца, шт': 2,
            'молоко, л': 0.1,
            'соль, ч.л.': 0.5,
        }
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    # count = int(request.GET.get("servings", 1))
    context = {
        'recipe': {
            'макароны, г': 0.3,
            'сыр, г': 0.05
        }
    }

    return render(request, 'calculator/index.html', context)


def hod_dog(request):
    # count = int(request.GET.get("servings", 1))
    context = {
        'recipe': {
            'булка, шт': 1,
            'сосиська, шт': 1,
            'горчица, г': 10,
        }
    }

    return render(request, 'calculator/index.html', context)

def mack_chicken(request):
    # count = int(request.GET.get("servings", 1))
    context = {
        'recipe': {
            'булочка, ломтик': 2,
            'куринное филе, ломтик': 1,
            'сыр, ломтик': 1,
            'лук, ломтик': 1,
            'салат, лист': 1,
        }
    }

    return render(request, 'calculator/index.html', context)