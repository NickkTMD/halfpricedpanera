# send web requests to log into panera and change name

import requests

login_url = "https://www-api.panerabread.com/www-api/public/session/login/panera"
update_url = "https://www-api.panerabread.com/www-api/user/update"

email = "nsgebo@gmail.com"
password = "<PASS>"


def login(email, password):
    # login
    login_body = {
        "email": email,
        "password": password
    }

    login_headers = {

        "accept": "application/json, text/plain, */*",
        "content-type": "application/json;charset=UTF-8",

    }


    # simulate cors preflight req
    preflight_headers = {
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json;charset=UTF-8",
        "origin": "https://www.panerabread.com",
        "access-control-request-method": "POST",
        "access-control-request-headers": "content-type"
    }

    preflight_url = "https://www-api.panerabread.com/www-api/public/session/login/panera"
    preflight = requests.options(preflight_url, headers=preflight_headers)
    print(preflight.headers)
    print(preflight.text)

    # use preflight to send actual request






    # send login request
    x = requests.post(login_url, json=login_body, headers=login_headers)
    print(x.headers)
    print(x.text)


    # get token
    # accessToken = x.json()["accessToken"]
    # print(accessToken)

def update_name():
    # update name
    first_name = "John"
    last_name = "Doe"

    ORIGIN_SOURCE = "iWeb"
    ACCESS_TOKEN = "<place here>"

    update_body = {"firstName": first_name,
                   "lastName": last_name,
                   "isEmailGlobalOpt": True,
                   "isDoNotShare": False,
                   "username": "nsgebo@gmail.com"
                   }

    update_headers = {

                "accept": "application/json, text/plain, */*",
                # "accept-language": "en-US,en;q=0.9",
                "content-type": "application/json;charset=UTF-8",
                # "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\"",
                # "sec-ch-ua-mobile": "?0",
                # "sec-ch-ua-platform": "\"Windows\"",
                # "sec-fetch-dest": "empty",
                # "sec-fetch-mode": "cors",
                # "sec-fetch-site": "same-site",
                "x-access-token": ACCESS_TOKEN,
                "x-origin-source": ORIGIN_SOURCE,
                # "x-session-trace-id": "T375137cd-ab66-4214-83ea-2946d8cc5189T"

                        }

    x = requests.put(update_url, json=update_body, headers=update_headers)

    print(x.headers)
    print(x.text)


login(email, password)