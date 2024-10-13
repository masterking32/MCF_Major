# Developed by: MasterkinG32
# Date: 2024
# Github: https://github.com/masterking32
# Telegram: https://t.me/MasterCryptoFarmBot


class Squads:
    def __init__(self, log, httpRequest, account_name):
        self.log = log
        self.http = httpRequest
        self.account_name = account_name

    def get_squad(self, squad_id):
        try:
            response = self.http.get(
                url=f"/api/squads/{squad_id}",
                display_errors=False,
                send_option_request=False,
            )

            if response is None:
                self.log.error(
                    f"<r>⭕ <c>{self.account_name}</c> failed to get squad!</r>"
                )
                return None

            return response
        except Exception as e:
            self.log.error(f"<r>⭕ <c>{self.account_name}</c> failed to get squad!</r>")
            # self.log.error(f"<r>{e}</r>")
            return None

    def get_position(self, squad_id):
        try:
            response = self.http.get(
                url=f"/api/squads/top/position/{squad_id}/",
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
