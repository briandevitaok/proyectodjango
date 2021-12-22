from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# import stripe 


@login_required(login_url='login')
def crear(request):



    return render(request, 'metodos_pago/profile_pago.html',{
        
    })

   

    
