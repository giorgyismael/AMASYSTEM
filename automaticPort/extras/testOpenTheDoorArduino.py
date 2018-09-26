import requests as rqts

rqts.get("http://{}:{}/automaticport/resquestarduinoteste/{}/{}".format(
    ('191.52.62.19'),('8080'),('True'),('secretKey')), timeout=5,)