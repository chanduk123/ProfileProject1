from django.shortcuts import render

# Create your views here.
def getPage(request):
    return render(request,'index.html')

def getProfilePage(request):
    return  render(request,'UserProfile.html')
def saveUserProfile(request):
    userid=request.POST['uid']
    username=request.POST['uname']
    password=request.POST['pwd']
    email=request.POST['email']
    from ProfileApp.models import UserProfile
    up= UserProfile(email=email,userid=userid,password=password,username=username)
    up.save()
    return render(request,'index.html')
def updateProfile(request):
    return render(request,'UserProfile.html')
def deletePage(request):
    return render(request,'delete.html')
def deleteUserProfile(request):
    usrid=request.POST['uid']
    from ProfileApp.models import UserProfile
    UserProfile.objects.filter(userid=usrid).delete()
    return render(request,'index.html')
def displayUserProfiles(request):
    from ProfileApp.models import UserProfile
    UserProfiles=UserProfile.objects.all()
    return render(request,'display.html',{'userprofiles':UserProfiles})


