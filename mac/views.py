from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"modifiedhomepage.html")
def modifiedFAQpage(request):
    return render(request,"modifiedFAQpage.html")
def modifiedaboutpage(request):
    return render(request,"modifiedaboutpage.html")
def modifiedcontactpage(request):
    return render(request,"modifiedcontactpage.html")
def modifiednewdonatepage(request):
    return render(request,"modifiednewdonatepage.html")
def modifiedactivitypage(request):
    return render(request,"modifiedactivitypage.html")
def modifiednewcovidinfo(request):
    return render(request,"modifiednewcovidinfo.html")
def modifiednewgallerypage(request):
    return render(request,"modifiednewgallerypage.html")
def modifiedteampage(request):
    return render(request,"modifiedteampage.html")
def proceed(request):
    name = request.POST.get('Name', 'default')
    surname = request.POST.get('Surname', 'default')
    phone = request.POST.get('Phone', 'default')
    pincode = request.POST.get('Pincode', 'default')
    amount = request.POST.get('Amount', 'default')
    if (len(str(phone))==10 and len(str(pincode))==6 and len(str(amount))>1 and phone.isnumeric() and pincode.isnumeric() and amount.isnumeric()):
        params = {'Name': name, 'Surname': surname ,"Amount":amount}
        return render(request,"proceed.html",params)
    else:
        params = {'Name': name, 'Surname': surname}
        return render(request, "errorpage.html",params)
def otp(request):
    name = request.POST.get('Name', 'default')
    surname = request.POST.get('Surname', 'default')
    card = request.POST.get('card', 'default')
    cardp = request.POST.get('cardph', 'default')
    password = request.POST.get('password', 'default')
    slph=cardp[:6]+"XXXX"
    if(len(str(card))==16 and len(str(cardp))==10 and len(str(password))==6 and card.isnumeric() and cardp.isnumeric() and password.isnumeric() ):
        params={"no":slph,'Name': name, 'Surname': surname}
        return render(request,"OTPpage.html",params)
    else:
        params = {"no": slph}
        return render(request,"errorpage2.html")
def sucess(request):
    OTP= request.POST.get('OTP', 'default')


    if(len(str(OTP))==6 and OTP.isnumeric()):

        return render(request,"sucess.html")
    else:

        return render(request,"failed.html")