# -*- coding: utf-8 -*-
"""Creation of the User form, to ask for recommendation."""

from django.forms import Form, ChoiceField


class SelectUserForm(Form):
    """Form to select the user id for a recommendation."""
    CHOICES = (
        (45, 'Utilisateurn nº 45'),
        (678, 'Utilisateur nº 678'),
        (1256, 'Utilisateur nº 1256'),
        (3333, 'Utilisateur nº 3333'),
        (7868, 'Utilisateur nº 7868'),
        (12067, 'Utilisateur nº 12067'),
        (34777, 'Utilisateur nº 34777'),
        (45211, 'Utilisateur nº 45211'),
        (58990, 'Utilisateur nº 58990'),
        (61052, 'Utilisateur nº 61052'),
    )
    select_user = ChoiceField(label="Liste des utilisateurs :", choices=CHOICES)
