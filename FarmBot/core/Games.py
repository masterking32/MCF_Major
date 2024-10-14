# Developed by: MasterkinG32
# Date: 2024
# Github: https://github.com/masterking32
# Telegram: https://t.me/MasterCryptoFarmBot


import json
import random
import time
from mcf_utils.api import API


class Games:
    def __init__(self, log, httpRequest, account_name, license_key=None):
        self.log = log
        self.http = httpRequest
        self.account_name = account_name
        self.license_key = license_key

    def start_bonus(self):
        try:
            bonus = self.get_bonus()
            if bonus is None:
                self.log.info(
                    f"<g>✅ Game <c>{self.account_name}</c> already finished Hold coin!</g>"
                )
                return

            if bonus.get("detail") is not None:
                self.log.info(
                    f"<g>🎁 <c>{self.account_name}</c> already finished Hold coin!</g>"
                )
                return

            coin = random.randint(800, 900)
            self.log.info(
                f"<g>😴 <c>{self.account_name}</c> is starting the Hold coin, waiting for <c>60</c> seconds...</g>"
            )

            time.sleep(60)
            self.finish_bonus(coin)
            self.log.info(
                f"<g>🎁 <c>{self.account_name}</c> finished Hold coin and got <c>{coin}⭐</c> coins!</g>"
            )

        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to start Hold coin!</r>"
            )
            # self.log.error(f"<r>{e}</r>")

    def start_roulette(self):
        try:
            roulette = self.get_roulette()
            if roulette is None:
                self.log.info(
                    f"<g>✅ Game <c>{self.account_name}</c> already finished Roulette!</g>"
                )
                return

            if roulette.get("detail") is not None:
                self.log.info(
                    f"<g>🎰 <c>{self.account_name}</c> already finished Roulette!</g>"
                )
                return

            self.log.info(
                f"<g>🎰 <c>{self.account_name}</c> is starting the Roulette...</g>"
            )

            self.start_roulette_request()

            self.log.info(f"<g>🎁 <c>{self.account_name}</c> finished Roulette!</g>")

        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to start Roulette!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None

    def start_swipe_coin(self):
        try:
            swipe = self.get_swipe()
            if swipe is None:
                self.log.info(
                    f"<g>✅ Game <c>{self.account_name}</c> already finished Swipe coin!</g>"
                )
                return

            if swipe.get("detail") is not None:
                self.log.info(
                    f"<g>🪙 <c>{self.account_name}</c> already finished Swipe coin!</g>"
                )
                return

            self.log.info(
                f"<g>🪙 <c>{self.account_name}</c> is starting Swipe coin, waiting for 60 seconds...</g>"
            )

            time.sleep(60)
            coins = random.randint(2300, 2800)
            self.start_swipe_request(coins)

            self.log.info(
                f"<g>🎁 <c>{self.account_name}</c> finished Swipe coin and received <c>{coins}⭐</c> coins!</g>"
            )

        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to start Swipe coin!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None

    def start_durov(self):
        try:
            durov = self.get_durov()
            if durov is None:
                self.log.info(
                    f"<g>✅ Game <c>{self.account_name}</c> already finished Durov!</g>"
                )
                return

            if durov.get("detail") is not None:
                self.log.info(
                    f"<g>🎮 <c>{self.account_name}</c> already finished Durov!</g>"
                )
                return

            answer = self.get_api_durov_answer()
            if answer is None:
                self.log.info(
                    f"<y>🟡 <c>{self.account_name}</c>, the Durov game answer is not ready yet!</y>"
                )
                return

            task_answer = answer.get("task_value", None)

            if task_answer is None or len(task_answer) != 4:
                self.log.info(
                    f"<y>🟡 <c>{self.account_name}</c>, the Durov game answer is empty!</y>"
                )
                return

            self.log.info(
                f"<g>🎮 <c>{self.account_name}</c> is starting Durov game...</g>"
            )

            self.start_durov_request(task_answer)

            self.log.info(f"<g>🎁 <c>{self.account_name}</c> finished Durov game!</g>")

        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to start Durov!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None

    def start_durov_request(self, task_answer):
        try:
            response = self.http.post(
                url="/api/durov/",
                display_errors=False,
                send_option_request=False,
                valid_response_code=201,
                data=json.dumps(task_answer),
            )

            if response is None:
                self.log.error(
                    f"<r>⭕ <c>{self.account_name}</c> failed to start Durov!</r>"
                )
                return None

            return response
        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to start Durov!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None

    def get_durov(self):
        try:
            response = self.http.get(
                url="/api/durov/",
                display_errors=False,
                send_option_request=False,
            )

            if response is None:
                return None

            return response
        except Exception as e:
            self.log.error(f"<r>⭕ <c>{self.account_name}</c> failed to get Durov!</r>")
            # self.log.error(f"<r>{e}</r>")
            return None

    def get_swipe(self):
        try:
            response = self.http.get(
                url="/api/swipe_coin/",
                display_errors=False,
                send_option_request=False,
            )

            if response is None:
                return None

            return response
        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to get Swipe coin!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None

    def start_swipe_request(self, coins):
        try:
            response = self.http.post(
                url="/api/swipe_coin/",
                display_errors=False,
                send_option_request=False,
                valid_response_code=201,
                data=json.dumps({"coins": coins}),
            )

            if response is None:
                self.log.error(
                    f"<r>⭕ <c>{self.account_name}</c> failed to start Swipe coin!</r>"
                )
                return None

            return response
        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to start Swipe coin!</r>"
            )
            # self.log.error(f"<r>{e}</r>")

    def get_roulette(self):
        try:
            response = self.http.get(
                url="/api/roulette/",
                display_errors=False,
                send_option_request=False,
            )

            if response is None:
                return None

            return response
        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to get Roulette!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None

    def start_roulette_request(self):
        try:
            response = self.http.post(
                url="/api/roulette/",
                display_errors=False,
                send_option_request=False,
                valid_response_code=201,
                data=json.dumps({}),
            )

            if response is None:
                self.log.error(
                    f"<r>⭕ <c>{self.account_name}</c> failed to start Roulette!</r>"
                )
                return None

            return response
        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to start Roulette!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None

    def finish_bonus(self, coins):
        try:
            response = self.http.post(
                url="/api/bonuses/coins/",
                display_errors=False,
                send_option_request=False,
                data=json.dumps({"coins": coins}),
                valid_response_code=201,
            )

            if response is None:
                self.log.error(
                    f"<r>⭕ <c>{self.account_name}</c> failed to finish Hold coin!</r>"
                )
                return None

            return response
        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to finish Hold coin!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None

    def get_bonus(self):
        try:
            response = self.http.get(
                url="/api/bonuses/coins/",
                display_errors=False,
                send_option_request=False,
            )

            if response is None:
                return None

            return response
        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to get Hold coin!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None

    def get_api_durov_answer(self):
        if self.license_key is None:
            return None

        apiObj = API(self.log)
        data = {
            "game_name": "major",
            "action": "get_task",
            "task_type": "durov_game",
        }

        response = apiObj.get_task_answer(self.license_key, data)

        if "error" in response:
            if "license" in response["error"].lower():
                self.log.error(f"<y>⭕ API Error: {response['error']}</y>")
                self.log.error(f"<y>🟡 License key is invalid</y>")
                exit()
            return None
        elif "status" in response and response["status"] == "success":
            self.tasks = response["tasks"]
            return response
        elif (
            "status" in response
            and response["status"] == "error"
            and "message" in response
        ):
            # self.log.info(f"<y>🟡 {response['message']}</y>")

            if "license" in response["message"].lower():
                self.log.error(f"<y>🟡 License key is invalid</y>")
                exit()
            return None
        else:
            # self.log.error(
            #     f"<y>🟡 Unable to get task answer, please try again later</y>"
            # )
            return None
