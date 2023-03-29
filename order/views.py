from django.shortcuts import render

# Create your views here.

def first(request):
    if request.method=="POST":
        dict1=request.POST

        with open('data.csv','a') as csvfile:

            wrt = csv.writer(csvfile)

            for key, value in dict1.items():

                wrt.writerow([key,value])
               

    return render(request, 'ticket.html')
