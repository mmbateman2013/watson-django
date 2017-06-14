import sys
import os
import json
from django import forms
from models import Collection

class QueryForm(forms.Form):
    queryText = forms.CharField(max_length=1000, required=True)
    collection = forms.ModelMultipleChoiceField(queryset=Collection.objects.all().order_by('collectionName'), required=False)