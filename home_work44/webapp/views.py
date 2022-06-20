from django.shortcuts import render
from webapp.checker import check

def check_view(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        numbers = request.POST.get("numbers")
        message = check(numbers)
        print(message)


        return render(request, "index.html")
