# import packages
from django.shortcuts import render
from hcsProject.forms import SimpleForm
from chineseApp.RunModel import predictInput
from chineseApp.RunModel import getReviews
from django.views.generic import TemplateView, ListView

# home page with beer recommendation engine
def HomePageView(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SimpleForm(request.POST)

        # if the form has been filled out...
        if form.is_valid():

            # populate the form with the user input
            adj1 = form.cleaned_data['adj1']
            adj2 = form.cleaned_data['adj2']
            adj3 = form.cleaned_data['adj3']

            # create a list from the user input and pass it into the function in RunModel.py to predict the recommended beer styles
            adjs = [adj1, adj2, adj3]
            test = predictInput(adjs)[0:3]

            # get the best review for each predicted beer
            review1 = getReviews(test[0])
            review2 = getReviews(test[1])
            review3 = getReviews(test[2])

    # if the form has not been filled out yet...
    else:

        form = SimpleForm()

        # fill in dummy data so nothing prints to the screen in the HTML
        test = ["", "", ""]
        review1 = ""
        review2 = ""
        review3 = ""

    # Return all elements to the HTML
    return render(request, 'index.html', {'form': form, 'adjs': test, 'reviews': [review1, review2, review3]})


# Methodology page
class MethodologyView(TemplateView):
    template_name = "summary.html"
    