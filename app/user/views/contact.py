from django.shortcuts import render, redirect
from django.views import View
from user.models.contact import Contact
from django.core.mail import send_mail

class contact(View):

   def get(self, request):
        success_message = request.session.get('success_message')
        if success_message:
            del request.session['success_message']

        # Include the success message in the context
        context = {'success_message': success_message}
        
        return render(request, 'contact_me.html', context)
   
   def post(self, request):
       # saving user send data in variable
        postData = request.POST
        name =postData.get('name')
        email =postData.get('email')
        message =postData.get('message')
        contact = Contact(name=name, email=email,message=message)
        contact.contact_save()


        # sending email to myself
        from_email = 'kkarki761@gmail.com'
        admin_subject = f"New message from {name}"
        admin_message = f"Name: {name}\nEmail: {email}\nmessage:\n {message}"
        admin_email = 'kkarki7120@gmail.com'
        send_mail(admin_subject, admin_message, from_email,[admin_email], fail_silently=False )

        #sending email to client
        client_subject = "Thank you for messaging"
        client_message = f"Hello {name}. \n Thank you for your message. I will get back to you soon."
        send_mail(client_subject, client_message, from_email,[email], fail_silently=False)

        request.session['success_message'] = "Your response has been submitted. Thank you ! for your response."
        return redirect('contact')
   