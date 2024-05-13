from django.shortcuts import render
from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse


# Create your views here.

# def january(request):
#     return HttpResponse('<h1>Its january month<h1/>')

# def february(request):
#     return HttpResponse('<h1>Its february month<h1/>')

# def march(request):
#     return HttpResponse('<h1>Its march month<h1/>')

monthly_challenges = {
    'january' : 'Set SMART Goals : Define specific, measurable, achievable, relevant, and time-bound goals to give direction and purpose to your life.',
    'february':"Develop a Morning Routine : Start your day with positive habits such as meditation, exercise, journaling, or reading to set a productive tone for the rest of the day.",
    'march':"Practice Gratitude : Cultivate an attitude of gratitude by regularly expressing appreciation for the people, experiences, and opportunities in your life.",
    'april':"Learn Something New : Continuously seek opportunities to expand your knowledge and skills through lifelong learning, whether it's through books, courses, or hands-on experiences.",
    'may':"Embrace Failure : Embrace failure as a natural part of the learning process and use setbacks as opportunities for growth and improvement.",
    'june':"Take Risks : Step out of your comfort zone and take calculated risks to pursue your passions and achieve your goals.",
    'july':'Build Resilience : Develop resilience by learning to adapt to adversity, bounce back from setbacks, and overcome challenges with a positive mindset.',
    'august':'Prioritize Self-Care : Take care of your physical, mental, and emotional well-being by prioritizing self-care activities such as exercise, healthy eating, adequate sleep, and relaxation.',
    'september':'Cultivate Positive Relationships : Surround yourself with supportive and positive people who inspire, motivate, and challenge you to become the best version of yourself.',
    'october':'Practice Mindfulness : Cultivate mindfulness by staying present in the moment, practicing self-awareness, and observing your thoughts and emotions without judgment.',
    'november':"Give Back to Others : Find ways to contribute to your community and make a positive impact on the lives of others through acts of kindness, volunteering, or philanthropy.",
    'december': None

}

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, 'challenges/index.html', {
        'months': months
    })







def monthly_challenge_by_number(request,month):

    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('<h1>Invalid month</h1>')
    
    redirect_month = months[month - 1]
    redirect_path = reverse('month_challenge' , args=[redirect_month])
    return HttpResponseRedirect(redirect_path)




# def monthly_challenge(request,month):
#     challenge_text = None
#     if month == 'january':
#         challenge_text = '<h1>It january month<h1/>'
#     elif month == 'february':
#         challenge_text = '<h1>It february month<h1/>'
#     elif month == 'march':
#         challenge_text = '<h1>It march month<h1/>'
#     else:
#        return HttpResponseNotFound('<h1>This month is not supported</h1>')
#     return HttpResponse(challenge_text)

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = render(request, 'challenges/challenge.html' , {
            'text': challenge_text,
            'month_name':month
        })
        return response_data
    except:
       raise Http404()
    



















