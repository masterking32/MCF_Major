# Developed by: MasterkinG32
# Date: 2024
# Github: https://github.com/masterking32
# Telegram: https://t.me/MasterCryptoFarmBot

import json


class Auth:
    def __init__(self, log, httpRequest, account_name, tgWebData, ref_link=None):
        self.log = log
        self.http = httpRequest
        self.account_name = account_name
        self.tgWebData = tgWebData
        self.ref_link = ref_link

    def login(self):
        try:
            headers = {}
            if self.ref_link:
                headers = {"referer": self.ref_link}

            response = self.http.post(
                url="/api/auth/tg/",
                data=json.dumps({"init_data": self.tgWebData}),
                headers=headers,
                send_option_request=False,
            )

            if response is None:
                self.log.error(f"<r>⭕ <c>{self.account_name}</c> failed to login!</r>")
                return None

            access_token = response.get("access_token")
            self.http.authToken = f"Bearer {access_token}"

            self.log.info(
                f"<g>🟢 <c>{self.account_name}</c> successfully logged in to Major!</g>"
            )

            return response
        except Exception as e:
            self.log.error(f"<r>⭕ <c>{self.account_name}</c> failed to login!</r>")
            # self.log.error(f"<r>{e}</r>")
            return None
