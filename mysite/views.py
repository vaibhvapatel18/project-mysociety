from django.shortcuts import render
from mysite.models import Socity_Members,Events,Notice,Watchman,Visitors,Complaint
# Create your views here.
def index(request):
    try:
        request.session['name']
        user = Socity_Members.objects.get(name = request.session['name'])
        return render(request, 'index.html',{'user' :  user})
    except:
        return render(request, 'login.html')
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        try:
            user_object = Socity_Members.objects.get(name = request.POST['name'])
            if user_object.password == request.POST['password']:
                request.session['name'] = request.POST['name']
                return render(request, 'index.html',{'user': user_object})
            else:
                return render(request,'login.html')
        except:
            return render(request,'login.html', {'msg':" does't exits'"})

def  socity_members(request):
    user_object = Socity_Members.objects.get(name = request.session['name'])
    members = Socity_Members.objects.all()
    return render(request, 'societymember.html',{'users':members,'user':user_object})

def  profile(request):
    user = Socity_Members.objects.get(name = request.session['name'])
    # members = Socity_Members.objects.all()
    return render(request, 'profile.html',{'user':user})

def  events(request):
    events = Events.objects.all()
    user_object = Socity_Members.objects.get(name = request.session['name'])
    return render(request, 'event.html',{'events':events,'user':user_object})

def  visitors(request):
    visotors = Visitors.objects.all()
    user_object = Socity_Members.objects.get(name = request.session['name'])
    return render(request, 'visitors.html',{'visitors':visotors,'user':user_object})

def  watchman(request):
    watchman = Watchman.objects.all()
    user_object = Socity_Members.objects.get(name = request.session['name'])
    return render(request, 'watchman.html',{'watchman':watchman,'user':user_object})

def  notice(request):
    notice = Notice.objects.all()
    user_object = Socity_Members.objects.get(name = request.session['name'])
    return render(request, 'notice.html',{'notice':notice,'user':user_object})


def  myevent(request):
    if request.method == "GET":
        user_object = Socity_Members.objects.get(name = request.session['name'])
        return render(request, 'myevent.html',{'user':user_object})
    else:
        Events.objects.create(
        event_name=request.POST['name'],
        event_date=request.POST['date'],
        event_information=request.POST['data'],
        )
        events = Events.objects.all()
    user_object = Socity_Members.objects.get(name = request.session['name'])
    return render(request, 'event.html',{'events':events,'user':user_object})

def  complaint(request):
    if request.method == "GET":
        user_object = Socity_Members.objects.get(name = request.session['name'])
        return render(request, 'abc.html',{'user':user_object})
    else:
        Complaint.objects.create(
        notice_name=request.POST['name'],
        notice_date=request.POST['date'],
        notice_information=request.POST['data'],
        )
        events = Events.objects.all()
    user_object = Socity_Members.objects.get(name = request.session['name'])
    return render(request, 'index.html',{'events':events,'user':user_object})