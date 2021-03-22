import pytest
import json
import jsonpath
import requests

url1 = "http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow"
url2 = "https://api.stackexchange.com/2.2/answers?order=asc&sort=activity&site=stackoverflow"

def test_rest_assured_api():
    respose = requests.get(url1)

    for data in respose.json()['items']:
        if data['answer_count'] == 1:
            print(data['link'])
        else:
            print('Answer Count Skipped')
        print()

        if data['view_count'] > 0:
            print(data['view_count'])
        else:
            print("View Count skpped.")
        print()

        if data['score'] == 0:
            print(data['score'])
        else:
            print("User Not Registered.")
        print()


    print("Total Links are: " +str(len(data['link'])))
    print("Total Title Count: "+str(len(data['title'])))
    # print(respose.json()['items'])

def test_rest_assured_api_response():
    response = requests.get(url2)
    results1 = response.json()['items']

    for data in results1:
        print(data['question_id'], end=' ')
    print('***********************')

    results2 = response.json()['items']
    for users in results2:
        print(users['answer_id'], end=' ')
    print('***********************')

    result3 = response.json()['items'][0]
    for link in result3:
        print(link)
    print('************************')


    # Print value by the items > owner > [index]...

    results4 = response.json()['items'][0]['owner']
    for oner in results4:
        print(oner, end=' ')
    print('---END---')


    results5 = response.json()['items'][0]
    for oner in results4:
        print(oner)
    for mn in results5:
        print(mn)
    print()
    print('---END---')

def test_print_links():
    respose = requests.get(url1)
    for data in respose.json()['items']:
        if data['score'] > 0:
            print(data['link'])
        else:
            print('---- Empty Link Space ----')
        print()
    print()

