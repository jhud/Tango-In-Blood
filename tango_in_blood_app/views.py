from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

from tango_in_blood_app.models import Profile, User

from django.views.generic import TemplateView

class TeamView(TemplateView):
    def get(self, request, team_name):        
        return render(request, "team_view.html",
                {'team_name': team_name})
               
class ProfileView(TemplateView):
    @method_decorator(login_required)
    def get(self, request):        
        user_profile = request.user.get_profile()
        victims = User.objects.filter(profile_converted_bys=request.user)
        return render(request, "profile_view.html", {'user_profile': user_profile, 'victims': victims})
        
def checkpassword(request):
    new_username = request.POST['id_username']
    if request.user.is_authenticated():
        return HttpResponse("You are already logged in, you don't need this password!") 
    biter = Profile.objects.get(conversion_password__exact=request.POST['id_password']).user
    if (biter == None):
        return HttpResponse("Password failed!") 
    elif User.objects.filter(username__exact=new_username).exists():
        return HttpResponse("That username is taken!") 
    else:
        user = User.objects.create_user(new_username, password="vampire")
        user.converted_by = biter
        new_user = authenticate(username=new_username,
                                    password='vampire')
        login(request, new_user)
        return HttpResponse("You are in!") 
        
    