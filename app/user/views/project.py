from django.shortcuts import render, redirect
from django.views import View
from user.models.project import Project_Message
from django.core.mail import send_mail


class project(View):

    def get(self, request):
        success_message = request.session.get('success_message')
        if success_message:
            del request.session['success_message']

        # Include the success message in the context
        context = {'success_message': success_message}
        
        return render(request, 'project.html', context)
    
    def post(self, request):
        # saving user send data in variable
        postData = request.POST
        name =postData.get('name')
        email =postData.get('email')
        message =postData.get('message')
        project = postData.get('project')
        budget = postData.get('budget')
        project_message = Project_Message(name=name, email=email,message=message,project=project,budget=budget)
        project_message.project_message_save()


        # sending email to myself
        from_email = 'kkarki761@gmail.com'
        admin_subject = f"New message from {name}"
        admin_message = f"Name: {name}\nEmail: {email}\nproject Type: {project}\nEstimate budget: {budget}\nmessage:\n{message}"
        admin_email = 'kkarki7120@gmail.com'
        send_mail(admin_subject, admin_message, from_email,[admin_email], fail_silently=False )

        #sending email to client
        client_subject = "Thank you for willing to work with me."
        client_message = f"Hey {name}!\nGood to hear that you want to work with me. Thank you for your response and I will get back to you soon"
        send_mail(client_subject, client_message, from_email,[email], fail_silently=False)

        request.session['success_message'] = "Your response has been submitted. Thank you ! for your response."
        return redirect('project')





