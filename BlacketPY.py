import requests
import threading
import time
import random

legacy_url = "https://blacket.org/"
session = requests.Session()


class blacketErrors:
    class InvalidLogin(Exception):
        def __init__(self, message="Incorrect login please try again!"):
            self.message = message
            super().__init__(self.message)

        pass

    class FailedAuth(Exception):
        def __init__(self, message="The server declined to connect."):
            self.message = message
            super().__init__(self.message)

        pass

    class UnknownError(Exception):
        def __init__(self, message="An unidentified error has occurred!"):
            self.message = message
            super().__init__(self.message)

        pass

    class BadRequest(Exception):
        def __init__(self, message="Something went terribly wrong."):
            self.message = message
            super().__init__(self.message)

        pass


class BlacketPY:
    def login(user, password):
        login_res = session.post(
            legacy_url + "worker/user/login.php",
            headers={
                "authority": "blacket.org",
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "origin": "https://blacket.org",
                "pragma": "no-cache",
                "referer": "https://blacket.org/market/",
                "sec-ch-ua": '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
                "x-requested-with": "XMLHttpRequest",
            },
            data={
                "username": user,
                "password": password,
            },
        )
        if "SUCCESS" in login_res.text:
            return (
                "successfully logged in | PHPSESSID: %s"
                % login_res.cookies["PHPSESSID"]
            )  # returns login cookie as well.

        elif "Username and password don't match" in login_res.text:
            raise blacketErrors.InvalidLogin()

        else:
            raise blacketErrors.UnknownError()

    def buy_boxes(auth):
        box_types = [
            "Aquatic",
            "Blizzard",
            "Color",
            "Dino",
            "Ice Monster",
            "Medieval",
            "Safari",
            "Space",
            "Spooky",
            "Wonderland",
        ]
        box = random.choice(box_types)
        box_res = session.post(
            legacy_url + "worker/box/openbox.php",
            cookies={"PHPSESSID": auth},  # your sess id.
            headers={
                "authority": "blacket.org",
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "origin": "https://blacket.org",
                "pragma": "no-cache",
                "referer": "https://blacket.org/market/",
                "sec-ch-ua": '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
                "x-requested-with": "XMLHttpRequest",
            },
            data={"box": box},
        )
        if box in box_res.text:
            box_type = box_res.text.split("|")[0]
            box_rarity = box_res.text.split("|")[1]
            return "Successfully bought %s box and received %s (%s)!" % (
                box,
                box_type,
                box_rarity,
            )

        elif "You're being rate limited.":
            return "Rate Limited.."

        else:
            raise blacketErrors.UnknownError()

    def add_tokens(auth):
        token_res = session.post(
            legacy_url + "worker/box/openbox.php",
            cookies={"PHPSESSID": auth},
            headers={
                "authority": "blacket.org",
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9",
                "cache-control": "no-cache",
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                "origin": "https://blacket.org",
                "pragma": "no-cache",
                "referer": "https://blacket.org/market/",
                "sec-ch-ua": '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": '"Windows"',
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42",
                "x-requested-with": "XMLHttpRequest",
            },
            data="box=Add Tokens",
        )
        if "You're" in token_res.text:
            return "Please try again as the server is limited!"

        elif "images" in token_res.text:
            return "25k tokens were successfully added!"

        else:
            raise blacketErrors.UnknownError()
