# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-timeout
"""View for the web app of the app_web_p9 project.
"""
import os
import requests
from django.shortcuts import render
from .forms import SelectUserForm


def recommender(request):
    """
    View to a page where one can select a user id to get the recommendation.
    Request to  our REST API on Heroku to get the recommendation for that user.
    Return the page with the 5 articles recommendation.
    """
    # When the form has been posted.
    if request.method == "POST":
        # Checking if the form has been validated.
        select_user_form = SelectUserForm(request.POST)
        if select_user_form.is_valid():
            # Catching the form selected choice.
            select_user_id = select_user_form.cleaned_data["select_user"]
            # Request with the user id to the Recommender System in our REST API on Heroku.
            if os.environ.get("ENV") == "PRODUCTION":
                endpoint = f"https://ia-api-project9.herokuapp.com/recommender/?select_user_id={select_user_id}"
            else:
                endpoint = f"http://127.0.0.1:8080/recommender/?select_user_id={select_user_id}"
            response = requests.get(endpoint)
            reco = response.json()
            # What to render to the recommender template.
            context = {
                "select_user_id": select_user_id,
                "reco_list" : reco['reco']
                }
            # And redirect to the recommender page.
            return render(request, "recommender.html", context)

    # To display the empty select user form.
    else:
        select_user_form = SelectUserForm()

    # What to render to the user_request template.
    context = {"select_user_form": select_user_form}

    return render(request, "user_request.html", context)
