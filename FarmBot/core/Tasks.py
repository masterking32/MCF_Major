# Developed by: MasterkinG32
# Date: 2024
# Github: https://github.com/masterking32
# Telegram: https://t.me/MasterCryptoFarmBot


import json


class Tasks:
    def __init__(self, log, httpRequest, account_name):
        self.log = log
        self.http = httpRequest
        self.account_name = account_name

    def get_tasks(self, is_daily):
        try:
            response = self.http.get(
                url=(
                    "/api/tasks/?is_daily=true"
                    if is_daily
                    else "/api/tasks/?is_daily=false"
                ),
                display_errors=False,
                send_option_request=False,
            )

            if response is None:
                self.log.error(
                    f"<r>⭕ <c>{self.account_name}</c> failed to get tasks!</r>"
                )
                return None

            return response
        except Exception as e:
            self.log.error(f"<r>⭕ <c>{self.account_name}</c> failed to get tasks!</r>")
            # self.log.error(f"<r>{e}</r>")
            return None

    def check_task(self, task_id):
        try:
            response = self.http.post(
                url=f"/api/tasks/",
                display_errors=False,
                send_option_request=False,
                data=json.dumps({"task_id": task_id}),
                valid_response_code=201,
            )

            if response is None:
                self.log.error(
                    f"<r>⭕ <c>{self.account_name}</c> failed to check task!</r>"
                )
                return None

            return response
        except Exception as e:
            self.log.error(
                f"<r>⭕ <c>{self.account_name}</c> failed to check task!</r>"
            )
            # self.log.error(f"<r>{e}</r>")
            return None
