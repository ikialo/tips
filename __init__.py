
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred_obj = firebase_admin.credentials.Certificate('serviceAcc.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':''
	})


ref = db.reference("/")

games = ref.child("Rugby/").get()
print(type(games))

for x,y in games.items():
    print(x)
    for m, n in y.items():
        print(n['Name'])

    print("")
