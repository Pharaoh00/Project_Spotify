#! -*- coding:utf-8 -*-

import requests
import json
import time

while True:
    time_before = time.time()
    client_id = "a5410cad3aea48a88f7dccf4559f840c"
    client_secret = "3f73d5c3e5e24278ab240c434be37e71"

    grant_type = 'client_credentials'

    to_json = {}

    #Request based on Client Credentials Flow from https://developer.spotify.com/web-api/authorization-guide/

    #Request body parameter: grant_type Value: Required. Set it to client_credentials
    body_params = {'grant_type' : grant_type}

    #url='https://accounts.spotify.com/api/token'

    #response=requests.post(url, data=body_params, auth = (client_id, client_secret))

    #token_string = "BQBYYL4ypN9E6NpLAAk9Y4Bv-3PwyFNzNXpwnYDxDnkJZOqVBVsJ5zOgCj1wFurx27igJj0j1bvtWCdHMLYYKE8Q0TtCWnEj5A8f6LjPrLtDiKY6vVDhsXHHb1_3Q3rD_jheIBHfCDyn5MY2DvRDm2I8rsZQpZQVoxI"

    token_string = "BQAGfltogeJ52zkSQBKapNdnLzZ-kPBm46VES3WWQ5SPqPUp25MyfW-xPChPzS9jwMki4nh4_rc7TSDL9OuwMTw6elj1jlkf7pBi2GTpYpXU1FC_ZrKazCU1-w48hs0sTtQtyMF8Yc7IJxESnajyLeJKPPPdEXq8_tvvg9Bf"
    headers = {"Authorization": "Bearer {}".format(token_string)}
    #print(headers)
    #response = requests.get("https://api.spotify.com/v1/tracks/6Q9JOfr9vKi2Sa2SUAhSen" ,auth=(client_id, client_secret))
    #response = requests.get("https://api.spotify.com/v1/tracks/6Q9JOfr9vKi2Sa2SUAhSen" ,headers=headers)
    
    response = requests.get("https://api.spotify.com/v1/me/player" ,headers=headers)

    test = json.loads(response.text)
    with open("test.json", "w") as f:
        json.dump(test, f, indent=4)
            
    print("Nome da musica: {}".format(test["item"]["name"]))
    print("Tempo em MS: {}".format(test["progress_ms"]))
    time_after = time.time()
    delta_time = time_after - time_before
    print("Delta time: {}".format(delta_time))
    #time.sleep(1)

    #print(response.text)
