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

    def get_top_squads(self):
        try:
            response = self.http.get(
                url="/api/squads/?limit=100",
                display_errors=False,
                send_option_request=False,
            )

            if response is None:
                self.log.error(
                    f"<r>⭕ <c>{self.account_name}</c> failed to get squads!</r>"
                )
                return None

            return response
        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to get squads!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None

    def get_squad_members(self, squad_id):
        try:
            response = self.http.get(
                url=f"/api/squads/{squad_id}/members/",
                display_errors=False,
                send_option_request=False,
            )

            if response is None:
                self.log.error(
                    f"<r>⭕ <c>{self.account_name}</c> failed to get squad members!</r>"
                )
                return None

            return response
        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to get squad members!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None

    def join_squad(self, squad_id):
        try:
            squad = self.get_squad(squad_id)
            squad_members = self.get_squad_members(squad_id)
            squad_position = self.get_position(squad_id)
            join_squad_request = self.join_squad_request(squad_id)
            if join_squad_request is None:
                return None

            self.log.info(
                f"<cyan>{self.account_name}</cyan><g> | 🏆 Squad: <c>{squad['name']}</c></g>"
            )

            self.log.info(
                f"<cyan>{self.account_name}</cyan><g> | 🎖️ Squad Position: <c>{squad_position['position']}</c></g>"
            )

            self.log.info(
                f"<cyan>{self.account_name}</cyan><g> | 🎉 <c>{self.account_name}</c> joined squad!</g>"
            )

            return squad
        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to join squad!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None

    def join_squad_request(self, squad_id):
        try:
            response = self.http.post(
                url=f"/api/squads/{squad_id}/join/",
                display_errors=False,
                send_option_request=False,
                valid_response_code=200,
            )

            if response is None:
                self.log.error(
                    f"<r>⭕ <c>{self.account_name}</c> failed to join squad!</r>"
                )
                return None

            return response
        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to join squad!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None
