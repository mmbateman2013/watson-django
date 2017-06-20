from __future__ import unicode_literals
from django.db import models

class Environment(models.Model):
    environmentName = models.CharField(max_length=250)
    environmentIDString = models.CharField(max_length=36)
    
    def __str__(self):
        return self.environmentName+' '+self.environmentIDString
    
class Collection(models.Model):
    collectionName = models.CharField(max_length=250)
    collectionIDString = models.CharField(max_length=36)
    collectionLabel = models.CharField(max_length=50, default='No Label')
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.collectionName+' '+self.collectionIDString
    
    def get_collection_documents(self):
        from watson_developer_cloud import DiscoveryV1

        discovery = DiscoveryV1(username='{username}',password='{password}',version='2016-12-01')
        
    def getCollectionName(self):
        return self.collectionName

class Document(models.Model):
    documentName = models.CharField(max_length=250)
    documentIDString = models.CharField(max_length=36)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    documentFile = models.CharField(default='media/default.html')
    
    def __str__(self):
        return self.documentName+' '+self.documentIDString
        
class Google_Contact(models.Model):
    contact_resource_name = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200, default='')
    contact_phone_no = models.CharField(max_length=200, default='')
    def __str__(self):
        return self.contact_name

#TODO: Add Query Model
"""
    column: queryText
    column: queryResults (holds the JSON response from API)
"""