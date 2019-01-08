
import logging as log
from django.http import JsonResponse, HttpResponse
import json


#log.basicConfig(filename='mysite.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=log.INFO)


def get_activity(request):
    #log.info("Request reached get_mysite")
    return_dict =  {
     'activity': [{
         'date': '19-01-02 10:10:10',
         'naps': {
             'start': '13:00',
             'end': '15:00'
         },
         'food': {
             'breakfast': 'Home Food',
             'lunch': 'Almost',
             'snacks': 'Full'
         },
         'description': 'Had a fun day learning about wild animals',
         'hygiene': {
             'diaper': '2',
             'potty': 'No'
         },
         'mood': 'Good',
         'health': 'Good'
     }]
    }

    return_response = HttpResponse(json.dumps(return_dict), content_type='application/json')
    return return_response

def get_notification(request):
    #log.info("Request reached get_notification")
    #return_dict = {'count': 10, 'from': 'admin', 'message':'found at index'}
    return_dict = { 
                    "notification": [
                      {
	               "from": "Admin",
                       "msg_type": "notification",
	               "msg": "message",
	               "type": "general/health/food/leave",
	               "date": "yyyy-mm-dd HH:mm"
                      },
                      {
	               "from": "Sajive",
                       "msg_type": "notification",
	               "msg": "Please ensure he has his food entirely",
	               "type": "food",
	               "date": "2019-01-03 08:00"
                      },
                      {
	               "from": "Admin",
                       "msg_type": "notification",
	               "msg": "Please send diapers",
	               "type": "general",
	               "date": "2019-01-02 17:00"
                      },
                      {
	               "from": "Admin",
                       "msg_type": "event",
	               "msg": "New year celebration on 4-Jan-2019",
	               "type": "general",
	               "date": "2019-01-02 17:00"
                      },
                    ]
                  }

    return_response = HttpResponse(json.dumps(return_dict), content_type='application/json')
    #del return_dict, all_activities, d
    return return_response


def get_attendance(request):
    return_dict = {
	              "total": "180/200",
	              "2019-01": {
		              "attendance": ["H", "Y", "L", "SL", "Y", "W", "W"],
		              "2019-01-01": "New year",
		              "2019-01-26": "Republic Day"
	              },
	              "2018-12": {
		              "attendance": ["H", "Y", "L", "SL", "Y", "W", "W"],
		              "2018-12-25": "Christmas Holiday",
		              "2018-12-26": "Christmas Holiday"
	              },
	              "2018-11": {
		              "attendance": ["H", "Y", "L", "SL", "Y", "W", "W"]
	              },
	              "2018-10": {
		              "attendance": ["H", "Y", "L", "SL", "Y", "W", "W"],
		              "2018-10-02": "Gandhi Jayanti"
	              },
	              "2018-09": {
		              "attendance": ["H", "Y", "L", "SL", "Y", "W", "W", "H", "Y", "L", "SL", "Y", "W", "W"],
		              "2018-09-05": "Teachers day celebration",
		              "2018-09-15": "Sports day at arena mall"
	              }
                  }
    return_response = HttpResponse(json.dumps(return_dict), content_type='application/json')
    return return_response


def get_profile(request):
    return_dict = {'count': 10, 'day1': 'Todays activity'}
    return_dict = { 
                    "profile": {
	               "name": "Rebecca George",
                       "class": "Senior Toddler",
	               "school": "Klay, Mahadevpura",
	               "mobile1": "+91 9845098450",
	               "mobile": "+91 9845098450"
                      },
                    "family": {
	               "father": ["John Filson", "+91 9845098450", "john.filson@gmail.com"],
                       "mother": ["Claire Thomson", "+91 9845098451", "claire.t@yahoo.co.uk"],
                      },
                    "details": {
                       "gender": "boy",
	               "dob": "2015-09-10",
	               "weight": "14 kgs",
	               "height": "100 cm",
	               "language": "English, Hindi",
                       "allergy": "None"
                      },
                    "pictures": {
	               "date": "2019-01-02 16:00",
                       "images" : "url"
                      }
                  }


    return_response = HttpResponse(json.dumps(return_dict), content_type='application/json')
    return return_response

def page_notfound(request):
    #log.info("Request reached page_notfound")
    return_dict = {'message': 'Page Not Found'}
    return_response = HttpResponse(json.dumps(return_dict), content_type='application/json')
    #del return_dict, all_activities, d
    return return_response


def get_sneakpeek(request):
    return_dict = {"fileName":"Infant_Sneak_Peek_(18th_dec-_21ts_Dec).pdf","npages":7,"pages":[{"number":1,"tables":[]},{"number":2,"tables":[]},{"number":3,"tables":[]},{"number":4,"tables":[{"cells":[{"i":1,"j":1,"content":"•"},{"i":1,"j":2,"content":"To explore wild animals"},{"i":2,"j":1,"content":"•"},{"i":2,"j":2,"content":"To explore the concept : In and out"}]}]},{"number":5,"tables":[]},{"number":6,"tables":[]},{"number":7,"tables":[{"cells":[{"i":1,"j":1,"content":"Tune:"},{"i":1,"j":2,"content":"Teddy Bear, Teddy"},{"i":1,"j":3,"content":""},{"i":1,"j":4,"content":""},{"i":1,"j":5,"content":""},{"i":1,"j":6,"content":""},{"i":2,"j":1,"content":"bear"},{"i":2,"j":2,"content":""},{"i":2,"j":3,"content":""},{"i":2,"j":4,"content":""},{"i":2,"j":5,"content":""},{"i":2,"j":6,"content":"·1)"},{"i":3,"j":1,"content":""},{"i":3,"j":2,"content":""},{"i":3,"j":3,"content":"In"},{"i":3,"j":4,"content":"and"},{"i":3,"j":5,"content":"Out"},{"i":3,"j":6,"content":""}]},{"cells":[{"i":1,"j":1,"content":"Elli Elephant,"},{"i":1,"j":2,"content":"Elli"},{"i":1,"j":3,"content":"Elephant,"},{"i":1,"j":4,"content":"Tune: Open, shut them"},{"i":1,"j":5,"content":""},{"i":2,"j":1,"content":"Turn around,"},{"i":2,"j":2,"content":""},{"i":2,"j":3,"content":""},{"i":2,"j":4,"content":""},{"i":2,"j":5,"content":"Opening Song -"},{"i":3,"j":1,"content":"Elli Elephant,"},{"i":3,"j":2,"content":"Elli"},{"i":3,"j":3,"content":"Elephant,"},{"i":3,"j":4,"content":"In and Out"},{"i":3,"j":5,"content":"Tune: Where is"}]},{"cells":[{"i":1,"j":1,"content":"Touch the ground"},{"i":1,"j":2,"content":"(Move baby's hands gently making"},{"i":1,"j":3,"content":"Thumbkin?"},{"i":2,"j":1,"content":"Elli Elephant, Elli Elephant,"},{"i":2,"j":2,"content":"a curve with palm inwards)"},{"i":2,"j":3,"content":""},{"i":3,"j":1,"content":"Dance on your toes,"},{"i":3,"j":2,"content":"In and Out"},{"i":3,"j":3,"content":"Circle time Is starting"},{"i":4,"j":1,"content":"Elli Elephant, Elli Elephant,"},{"i":4,"j":2,"content":"(Move baby's hands gently making"},{"i":4,"j":3,"content":"Circle time Is starting"},{"i":5,"j":1,"content":"Touch your nose"},{"i":5,"j":2,"content":"a curve with palm outwards)"},{"i":5,"j":3,"content":"We will have fun"},{"i":6,"j":1,"content":"Elli Elephant, Elli Elephant,"},{"i":6,"j":2,"content":"In, in, in, in"},{"i":6,"j":3,"content":"We will have fun"},{"i":7,"j":1,"content":"Give a little clap"},{"i":7,"j":2,"content":""},{"i":7,"j":3,"content":"Children come and sit now"},{"i":8,"j":1,"content":""},{"i":8,"j":2,"content":"(Move baby's hands gently making"},{"i":8,"j":3,"content":""},{"i":9,"j":1,"content":"Elli Elephant, Elli Elephant,"},{"i":9,"j":2,"content":""},{"i":9,"j":3,"content":"Children come and sit now"},{"i":10,"j":1,"content":""},{"i":10,"j":2,"content":"a curve with palm inwards slowly)"},{"i":10,"j":3,"content":""},{"i":11,"j":1,"content":"Take a nap"},{"i":11,"j":2,"content":""},{"i":11,"j":3,"content":"Each and every one"},{"i":12,"j":1,"content":""},{"i":12,"j":2,"content":"Out, out, out"},{"i":12,"j":3,"content":""},{"i":13,"j":1,"content":""},{"i":13,"j":2,"content":""},{"i":13,"j":3,"content":""}]}]}]}

    return_response = HttpResponse(json.dumps(return_dict), content_type='application/json')
    return return_response
