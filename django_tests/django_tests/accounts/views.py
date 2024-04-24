from django.shortcuts import render

# Create your views here.


def my_view(request):

    currentuser_id = request.user.id
    currentuser = user.objects.get(currentuser_id)

    articles.objets.filter(user=currentuser)