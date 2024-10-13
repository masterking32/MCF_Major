# Developed by: MasterkinG32
# Date: 2024
# Github: https://github.com/masterking32
# Telegram: https://t.me/MasterCryptoFarmBot


class UserVisit:
    def __init__(self, log, httpRequest, account_name):
        self.log = log
        self.http = httpRequest
        self.account_name = account_name

    def get_streak(self):
        try:
            response = self.http.get(
                url="/api/user-visits/streak/",
                display_errors=False,
                send_option_request=False,
            )

            if response is None:
                self.log.error(
                    f"<r>⭕ <c>{self.account_name}</c> failed to get streak!</r>"
                )
                return None

            return response
        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to get streak!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None

    def get_visit(self):
        try:
            response = self.http.post(
                url="/api/user-visits/visit/",
                display_errors=False,
                send_option_request=False,
            )

            if response is None:
                self.log.error(
                    f"<r>⭕ <c>{self.account_name}</c> failed to get visit!</r>"
                )
                return None

            return response
        except Exception as e:
            self.log.error(f"<r>⭕ <c>{self.account_name}</c> failed to get visit!</r>")
            # self.log.error(f"<r>{e}</r>")
            return None
