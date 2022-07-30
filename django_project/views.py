from django.http import HttpResponse
from django.shortcuts import render
import requests
from pprint import pprint
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp


def index(request):
  return render(request,'index.html')

def submit(request):
  scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
  creds = ServiceAccountCredentials.from_json_keyfile_name("fivemadmen-fac757e6f0c5.json",scope)
  client = gspread.authorize(creds)

  sheet = client.open("Atlan Backend").sheet1

  data=[request.GET['name'],request.GET['email'],request.GET['city'],request.GET['colour']]
  sheet.insert_row(data)
  return render(request,'index.html')


def export(request):
  scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
  creds = ServiceAccountCredentials.from_json_keyfile_name("fivemadmen-fac757e6f0c5.json",scope)
  client = gspread.authorize(creds)

  sheet = client.open("Atlan Backend").sheet1
  
  data = sheet.get_all_records() 
  # store=pp(data)
  print(data)
  
  return render(request,'export.html',{"data":data})