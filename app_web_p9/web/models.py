# -*- coding: utf-8 -*-
# pylint: disable=too-few-public-methods,no-member,missing-class-docstring
"""The Image model to store images, respective mask and
the predictive mask to get from the REST API.
"""
# from django.conf import settings
from django.db import models
from django.utils.html import mark_safe


class User(models.Model):
    """
    To create the User table in the database.
    """
    user_id = models.PositiveIntegerField(
        "Id de l'utilisateur", unique=True)

    class Meta:
        verbose_name = "User id"

    def __str__(self):
        return f"User id: {self.user_id}"
    

class Article(models.Model):
    """
    To create the Article table in the database.
    """
    # user_id = models.ManyToManyField(
    #     settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
    #     related_name="articles", verbose_name="Utilisateur")
    article_id = models.PositiveIntegerField(
        "Id de l'article", unique=True)
    users = models.ManyToManyField(
        User, related_name="articles", verbose_name="Utilisateur")

    def pred_mask_preview(self):
        """Displaying the recommended list of articles."""
        if self.mask_pred:
            return mark_safe(f'<img src="{self.mask_pred.url}" width="360" height="180"/>')
        return None

    class Meta:
        verbose_name = "Article"

    def __str__(self):
        return f"Article id: {self.article_id}"
    