# Developed by: MasterkinG32
# Date: 2024
# Github: https://github.com/masterking32
# Telegram: https://t.me/MasterCryptoFarmBot
import random
import sys
import os
import time

from utilities.utilities import getConfig
from .core.HttpRequest import HttpRequest
from .core.Auth import Auth
from .core.Users import Users
from .core.Squads import Squads
from .core.UserVisit import UserVisit
from .core.Tasks import Tasks
from .core.Games import Games

MasterCryptoFarmBot_Dir = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__ + "/../../"))
)
sys.path.append(MasterCryptoFarmBot_Dir)


class FarmBot:
    def __init__(
        self,
        log,
        bot_globals,
        account_name,
        web_app_query,
        proxy=None,
        user_agent=None,
        isPyrogram=False,
        tgAccount=None,
    ):
        self.log = log
        self.bot_globals = bot_globals
        self.account_name = account_name
        self.web_app_query = web_app_query
        self.proxy = proxy
        self.user_agent = user_agent
        self.isPyrogram = isPyrogram
        self.tgAccount = tgAccount

    async def run(self):
        try:
            self.log.info(
                f"<cyan>{self.account_name}</cyan><g> | 🤖 Start farming Major ...</g>"
            )

            self.http = HttpRequest(
                log=self.log,
                proxy=self.proxy,
                user_agent=self.user_agent,
                tgWebData=self.web_app_query,
                account_name=self.account_name,
            )

            ref_link = None
            if (
                self.isPyrogram
                and self.tgAccount is not None
                and self.tgAccount.NewStart
            ):
                ref_link = f"https://major.bot/?tgWebAppStartParam={self.tgAccount.ReferralToken}"

            auth = Auth(
                log=self.log,
                httpRequest=self.http,
                account_name=self.account_name,
                tgWebData=self.web_app_query,
                ref_link=ref_link,
            )

            login = auth.login()
            if login is None:
                return

            if "user" not in login or "id" not in login["user"]:
                self.log.error(f"<r>⭕ {self.account_name} failed to login!</r>")
                return

            user_id = login["user"]["id"]

            users = Users(
                log=self.log, httpRequest=self.http, account_name=self.account_name
            )

            user = users.get_user(user_id)
            if user is None:
                return

            rating = user.get("rating", 0)
            squad_id = user.get("squad_id", None)

            self.log.info(
                f"<cyan>{self.account_name}</cyan><g> | 🪙 Rating: <c>{rating}⭐</c></g>"
            )

            position = users.get_position(user_id)
            if position is None:
                return

            position = position.get("position", 0)

            self.log.info(
                f"<cyan>{self.account_name}</cyan><g> | 🥇 Position: <c>{position}</c></g>"
            )

            squad = Squads(
                log=self.log, httpRequest=self.http, account_name=self.account_name
            )

            user_squad = None
            user_squad_position = None
            if squad_id is not None:
                user_squad = squad.get_squad(squad_id)
                user_squad_position = squad.get_position(squad_id)

                if user_squad is not None and user_squad_position is not None:
                    user_squad = user_squad.get("name", None)
                    user_squad_position = user_squad_position.get("position", 0)

                    self.log.info(
                        f"<cyan>{self.account_name}</cyan><g> | 🏆 Squad: <c>{user_squad}</c></g>"
                    )
                    self.log.info(
                        f"<cyan>{self.account_name}</cyan><g> | 🎖️ Squad Position: <c>{user_squad_position}</c></g>"
                    )

            user_visit = UserVisit(
                log=self.log, httpRequest=self.http, account_name=self.account_name
            )

            self.log.info(
                f"<cyan>{self.account_name}</cyan><g> | 🔃 Sending basic requests ...</g>"
            )

            self.log.info(
                f"<cyan>{self.account_name}</cyan><g> | 📅 Getting daily streak ...</g>"
            )
            streak = user_visit.get_streak()

            self.log.info(
                f"<cyan>{self.account_name}</cyan><g> | 📊 Getting top users ...</g>"
            )
            top_users = users.get_top_users()

            self.log.info(
                f"<cyan>{self.account_name}</cyan><g> | 📈 Getting user referrals ...</g>"
            )
            user_referrals = users.get_user(user_id)

            license_key = self.bot_globals.get("license", None)
            tasks = Tasks(
                log=self.log,
                httpRequest=self.http,
                account_name=self.account_name,
                tgAccount=self.tgAccount,
                license_key=license_key,
                bot_globals=self.bot_globals,
            )

            self.log.info(
                f"<cyan>{self.account_name}</cyan><g> | 📋 Getting tasks ...</g>"
            )
            all_tasks = tasks.get_tasks(is_daily=False)

            self.log.info(
                f"<cyan>{self.account_name}</cyan><g> | 📋 Getting daily tasks ...</g>"
            )
            daily_tasks = tasks.get_tasks(is_daily=True)

            self.log.info(
                f"<cyan>{self.account_name}</cyan><g> | 👥 Getting squad ...</g>"
            )
            top_squads = squad.get_top_squads()

            visit = user_visit.get_visit()
            if visit is not None:
                is_increased = visit.get("is_increased", False)
                is_allowed = visit.get("is_allowed", False)
                streak = visit.get("streak", 0) + 1

                if is_increased and is_allowed:
                    self.log.info(
                        f"<cyan>{self.account_name}</cyan><g> | 📅 Streak increased to <c>{streak}</c>!</g>"
                    )
                elif is_allowed == False and self.tgAccount is not None:
                    if getConfig("join_channels", False):
                        await self.tgAccount.joinChat("starsmajor")
                        await time.sleep(5)
                    finish_task = tasks.check_task(15027)
                    if finish_task is not None:
                        self.log.info(
                            f"<cyan>{self.account_name}</cyan><g> | 🎉 Task <c>Join Major Channel</c> finished!</g>"
                        )

            user = users.get_user(user_id)

            if squad_id is None and top_squads is not None:
                random_squad = random.choice(top_squads[:4])
                squad_id = random_squad.get("id", None)
                squad_name = random_squad.get("name", None)
                self.log.info(
                    f"<cyan>{self.account_name}</cyan><g> | 🏆 Joining squad <c>{squad_name}</c> ...</g>"
                )
                squad.join_squad(squad_id)

            games = Games(
                log=self.log,
                httpRequest=self.http,
                account_name=self.account_name,
                license_key=license_key,
            )

            self.log.info(
                f"<cyan>{self.account_name}</cyan><g> | 🎮 Starting games ...</g>"
            )

            if getConfig("play_bonus", True):
                games.start_bonus()

            if getConfig("play_roulette", True):
                games.start_roulette()

            if getConfig("play_swipe_coin", True):
                games.start_swipe_coin()

            if getConfig("play_durov", True):
                games.start_durov()

            if getConfig("auto_finish_tasks", True):
                self.log.info(
                    f"<cyan>{self.account_name}</cyan><g> | 📋 Checking one-time tasks ...</g>"
                )
                await tasks.claim_tasks(all_tasks)
                self.log.info(
                    f"<cyan>{self.account_name}</cyan><g> | 📋 Checking daily tasks ...</g>"
                )
                await tasks.claim_tasks(daily_tasks)

            self.log.info(
                f"<cyan>{self.account_name}</cyan><g> | 🤖 Major farming finished!</g>"
            )

        except Exception as e:
            self.log.error(f"<r>⭕ {self.account_name} failed to farm!</r>")
            self.log.error(f"<r>{str(e)}</r>")
            return
        finally:
            delay_between_accounts = getConfig("delay_between_accounts", 60)
            random_sleep = random.randint(0, 20) + delay_between_accounts
            self.log.info(
                f"<g>⌛ Farming for <c>{self.account_name}</c> completed. Waiting for <c>{random_sleep}</c> seconds before running the next account...</g>"
            )
            time.sleep(random_sleep)
