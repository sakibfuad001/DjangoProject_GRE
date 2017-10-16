from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

#not required this function
@login_required
def account_redirect(request):
   # render(request,'home.html')
    return redirect(home_view, pk=request.user.pk, name=request.user.username)
#######


def home_view(request):

     return render(request, 'home.html' )



