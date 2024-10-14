# Developed by: MasterkinG32
# Date: 2024
# Github: https://github.com/masterking32
# Telegram: https://t.me/MasterCryptoFarmBot


import asyncio
import json
import random
import time

from utilities.utilities import getConfig
from mcf_utils.api import API
from mcf_utils.tgAccount import tgAccount as TG


class Tasks:
    def __init__(
        self,
        log,
        httpRequest,
        account_name,
        tgAccount=None,
        license_key=None,
        bot_globals=None,
    ):
        self.log = log
        self.http = httpRequest
        self.account_name = account_name
        self.tgAccount = tgAccount
        self.license_key = license_key
        self.bot_globals = bot_globals

    async def claim_tasks(self, tasks):
        if tasks is None:
            return

        for task in tasks:
            try:
                if task.get("is_completed", True):
                    continue

                task_name = task.get("title")
                task_type = task.get("type")
                task_id = task.get("id")

                if task_type in [
                    "watch_youtube",
                    "without_check",
                    "stories",
                ]:
                    self.log.info(
                        f"<g>📃 <c>{self.account_name}</c> is starting <c>{task_name}</c>!</g>"
                    )
                    self.check_task(task_id)
                elif task_type == "subscribe_channel" and self.tgAccount is not None:
                    if not getConfig("auto_finish_tasks", False):
                        continue

                    channel_url = task.get("payload", {}).get("url")
                    if channel_url is None or channel_url == "":
                        continue

                    if "+" not in channel_url:
                        channel_url = (
                            channel_url.replace("https://t.me/", "")
                            .replace("@", "")
                            .replace("boost/", "")
                        )

                        channel_url = (
                            channel_url.split("/")[0]
                            if "/" in channel_url
                            else channel_url
                        )

                    self.log.info(
                        f"<g>📃 <c>{self.account_name}</c> is starting <c>{task_name}</c>!</g>"
                    )
                    try:
                        if self.tgAccount is not None:
                            await self.tgAccount.joinChat(channel_url)
                    except Exception as e:
                        pass
                    await asyncio.sleep(5)

                    self.check_task(task_id)
                elif task_type == "code":
                    continue
                elif task_type == "external_api":
                    if not getConfig("start_bots", True):
                        continue

                    url = task.get("payload", {}).get("url")

                    if url is None or url == "" or "t.me/" not in url:
                        continue

                    data = {
                        "task_type": "invite",
                        "task_data": url,
                    }

                    api_response = self.get_api_data(data, license_key=self.license_key)
                    if (
                        api_response is None
                        or "status" not in api_response
                        or api_response["status"] != "success"
                    ):
                        continue

                    ref_link = api_response.get("referral")
                    bot_id = api_response.get("bot_id")

                    if ref_link is None or bot_id is None:
                        continue

                    self.log.info(
                        f"<g>🚀 Starting bot <c>{task.get('name', '')}</c>...</g>"
                    )

                    try:
                        tg = TG(
                            bot_globals=self.bot_globals,
                            log=self.log,
                            accountName=self.account_name,
                            proxy=self.http.proxy,
                            BotID=bot_id,
                            ReferralToken=ref_link,
                            MuteBot=True,
                        )

                        await tg.getWebViewData()

                        self.log.info(f"<g>✅ Bot <c>{bot_id}</c> started!</g>")

                        await asyncio.sleep(5)
                    except Exception as e:
                        pass

                    self.log.info(
                        f"<g>📃 <c>{self.account_name}</c> is starting <c>{task_name}</c>!</g>"
                    )

                    self.check_task(task_id)

                else:
                    continue
            except Exception as e:
                # self.log.error(f"<r>{e}</r>")
                continue

            time.sleep(random.randint(5, 10))

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
                # self.log.error(
                #     f"<r>⭕ <c>{self.account_name}</c> failed to check task!</r>"
                # )
                return None

            return response
        except Exception as e:
            # self.log.error(
            #     f"<r>⭕ <c>{self.account_name}</c> failed to check task!</r>"
            # )
            # self.log.error(f"<r>{e}</r>")
            return None

    def get_api_data(self, data, license_key):
        if license_key is None:
            return None

        apiObj = API(self.log)
        data["game_name"] = "major"
        data["action"] = "get_task"
        response = apiObj.get_task_answer(license_key, data)
        time.sleep(3)
        if "error" in response:
            self.log.error(f"<y>⭕ API Error: {response['error']}</y>")
            return None
        elif "status" in response and response["status"] == "success":
            return response
        elif (
            "status" in response
            and response["status"] == "error"
            and "message" in response
        ):
            self.log.info(f"<y>🟡 {response['message']}</y>")
            return None
        else:
            self.log.error(
                f"<y>🟡 Unable to get task answer, please try again later</y>"
            )
            return None
