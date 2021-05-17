import requests, urllib3, xmltodict, json

from celery import shared_task



@shared_task
def sum(a, b):
    print(a+b)
    return a+b
