from django.shortcuts import render


def author_list(request):
    return render(request, 'author_list.html')
