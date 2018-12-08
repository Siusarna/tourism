from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import auth, messages
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from .models import Contact

#Форма обратной связи
def feedback(request):
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['name']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']
			recipients = ['charodeyrap@gmail.com']
			try:
				send_mail(subject, message, email, recipients,)
			except BadHeaderError: #Защита от уязвимости
				return HttpResponse('Invalid header found')
			post = form.save()
			post.save()
			return redirect( '/')
	else:
			form = ContactForm()
	return render(request, 'feedback.html', {'form': form })
# Create your views here.

# Create your views here.
