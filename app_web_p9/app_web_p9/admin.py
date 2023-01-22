"""Overinding the default Admin with custom Project 9 header, site title and index title.
    """
from django.contrib.admin import AdminSite


class P8Admin(AdminSite):
    """Project 9 header, site title and index title."""
    site_header = 'Projet 9 | Administration'
    site_title = 'Projet 9 | Site Admin'
    index_title = "Réalisez une application de recommandation de contenu - \
        Projet 9 | Admin Home"
   