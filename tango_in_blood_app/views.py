from django.shortcuts import render

from django.views.generic import TemplateView

class TeamView(TemplateView):
    def get(self, request, team_name):        
        return render(request, "team_view.html",
                {'team_name': team_name})