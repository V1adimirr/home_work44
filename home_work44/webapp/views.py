from django.shortcuts import render
from webapp.checker import check, result_game

def check_view(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        numbers = request.POST.get("numbers")
        message = check(numbers)
        if message == list():
            message = result_game(numbers)

        context = {
            "text": message
        }


        return render(request, "result.html", context)
