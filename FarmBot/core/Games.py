# Developed by: MasterkinG32
# Date: 2024
# Github: https://github.com/masterking32
# Telegram: https://t.me/MasterCryptoFarmBot


import json
import random
import time


class Games:
    def __init__(self, log, httpRequest, account_name):
        self.log = log
        self.http = httpRequest
        self.account_name = account_name

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
                f"<g>🎁 <c>{self.account_name}</c> finished Hold coin and got <c>{coin}</c> coins!</g>"
            )

        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to start Hold coin!</r>"
            )
            # self.log.error(f"<r>{e}</r>")

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
