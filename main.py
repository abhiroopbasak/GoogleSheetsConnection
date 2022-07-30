import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("fivemadmen-fac757e6f0c5.json",scope)
client = gspread.authorize(creds)

sheet = client.open("Atlan Backend").sheet1   
data = sheet.get_all_records() 
# pp(data)


# print("Enter number of data to be added:",end='')
# n=int(input())
# for i in range(n):
#     data=[]
#     print("Name: ",end='')
#     data.append(input())
#     print("Email: ",end='')
#     data.append(input())
#     print("Gender: ",end='')
#     data.append(input())
#     print("Phone number: ",end='')
#     data.append(input())

#     sheet.insert_row(data)
requests = []
body = {
    'requests': requests
}
response = sheet.spreadsheets().batchUpdate(
    spreadsheetId=646396187,
    body=body).execute()
find_replace_response = response.get('replies')[1].get('findReplace')
print('{0} replacements made.'.format(
    find_replace_response.get('occurrencesChanged')))