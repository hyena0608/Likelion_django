from django.shortcuts import render

# Create your views here.
def team(request):
    return render(request, 'team.html')

def welcome(request):
    context = request.GET['context']

    teamList = context.split(',')


    return render(request, 'welcome.html', {'context' : context, 'teamCount' : len(teamList), 'teamList': teamList})