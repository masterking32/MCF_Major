# Developed by: MasterkinG32
# Date: 2024
# Github: https://github.com/masterking32
# Telegram: https://t.me/MasterCryptoFarmBot


class Users:
    def __init__(self, log, httpRequest, account_name):
        self.log = log
        self.http = httpRequest
        self.account_name = account_name

    def get_user(self, user_id):
        try:
            response = self.http.get(
                url=f"/api/users/{user_id}/",
                display_errors=False,
                send_option_request=False,
            )

            if response is None:
                self.log.error(
                    f"<r>⭕ <c>{self.account_name}</c> failed to get user!</r>"
                )
                return None

            return response
        except Exception as e:
            self.log.error(f"<r>⭕ <c>{self.account_name}</c> failed to get user!</r>")
            # self.log.error(f"<r>{e}</r>")
            return None

    def get_position(self, user_id):
        try:
            response = self.http.get(
                url=f"/api/users/top/position/{user_id}/",
                display_errors=False,
                send_option_request=False,
            )

            if response is None:
                self.log.error(
                    f"<r>⭕ <c>{self.account_name}</c> failed to get position!</r>"
                )
                return None

            return response
        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to get position!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None

    def get_top_users(self):
        try:
            response = self.http.get(
                url="/api/users/top/?limit=100",
                display_errors=False,
                send_option_request=False,
            )

            if response is None:
                self.log.error(
                    f"<r>⭕ <c>{self.account_name}</c> failed to get top users!</r>"
                )
                return None

            return response
        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to get top users!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None

    def get_referrals(self):
        try:
            response = self.http.get(
                url="/api/users/referrals/",
                display_errors=False,
                send_option_request=False,
            )

            if response is None:
                self.log.error(
                    f"<r>⭕ <c>{self.account_name}</c> failed to get referrals!</r>"
                )
                return None

            return response
        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to get referrals!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None
