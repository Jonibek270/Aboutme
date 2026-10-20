from django.shortcuts import render
def home_page(request):

    context = {
        'ism':'Name:Jonibek',
        'familiya':'Surname:Navruzov',
        'education':'Education place:Acharya University',
        'age':'Age:19',
        'birth':'Birth place:Bukhara',
    }
    return render(request,'homepage.html',context)