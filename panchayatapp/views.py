from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from rest_framework import status
from django.contrib.auth import authenticate
from nagarpanchayat.settings import EMAIL_HOST_USER
from panchayatapp.models import regesterComplaintes,registerUser,waterApplication

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        email_subject = 'New contact form submission'
        email_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        email = EmailMessage(email_subject, email_body, to=[EMAIL_HOST_USER])
        email.send()

        return render(request, 'home.html', {'success': True})

    return render(request, 'home.html')

def registercomplaintesView(request):
    if request.method == 'POST':
        fullName =  request.POST.get('fullName')
        wardNo = request.POST.get('wardNo')
        place = request.POST.get('place')
        complaintes = request.POST.get('complaintes')
        aboutComplaintes = request.POST.get('aboutComplaintes')

        complaint = regesterComplaintes(
            fullName = fullName,
            wardNo = wardNo,
            place = place,
            complaintes = complaintes,
            aboutComplaintes = aboutComplaintes
        )
        complaint.save()
        return redirect('home')

    return render(request, 'home.html')

def waterConectionView(request):
    if request.method == 'POST':
        fullName =  request.POST.get('fullName')
        wardNo = request.POST.get('wardNo')
        place = request.POST.get('place')
        houseNo = request.POST.get('houseNo')
        
        waterApply = waterApplication(
            fullName = fullName,
            wardNo = wardNo,
            place = place,
            houseNo = houseNo,
            
        )
        waterApply.save()
        return redirect('home')

    return render(request, 'home.html')

def loginView(request):
    if request.method =='POST':
        houseNo = request.POST.get('houseNo')
        fullName = request.POST.get('householderName')
        user = authenticate(houseNo= houseNo, fullName=fullName)
        if user is not None:
            return Response({'msg':'login Successfull'},
            status=status.HTTP_201_CREATED)
        else:
            return Response({'errors':{'non_field_errors':
            ['Email Or Password is not valid']}},
            status=status.HTTP_404_NOT_FOUND)

    return render(request, 'home.html')