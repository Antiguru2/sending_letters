from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from .models import Mail_sending  # sending_letters
from .forms import MailForm
from django.http import Http404



def index(request):    # для первичного тестирования, подлежит удалению
    print("index")
    form = MailForm()
    return render(request, 'index.html', {'form': form})




def sendemail(request):

    if request.method == 'POST':                                        
        form = MailForm(request.POST)
        if form.is_valid(): 
            mail_adres = form.cleaned_data['Mail']
            Mail_sending.objects.create(                
                        Mail=mail_adres 
                    )

            message = EmailMessage(
                        'subject',
                        'Добрый день! Архив прикрепьен к письму.',
                        'programist90@yandex.ru',
                        [mail_adres,],
                        
                    )

            message.attach_file('mail/file/victoria_setup.zip')
            message.send()
            
            return redirect("index")
        
        else:
            raise Http404()

    else:
        raise Http404()






