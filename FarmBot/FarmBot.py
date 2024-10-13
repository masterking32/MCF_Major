# Developed by: MasterkinG32
# Date: 2024
# Github: https://github.com/masterking32
# Telegram: https://t.me/MasterCryptoFarmBot
import sys
import os

from .core.HttpRequest import HttpRequest
from .core.Auth import Auth
from .core.Users import Users
from .core.Squads import Squads
from .core.UserVisit import UserVisit
from .core.Tasks import Tasks

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
        self.log.info(
            f"<cyan>{self.account_name}</cyan><g> | 🤖 Start farming Major ...</g>"
        )

        self.web_app_query = self.web_app_query.replace(
            "%2522allows_write_to_pm",
            "%2522is_premium%2522%253Atrue%252C%2522allows_write_to_pm",
        )

        self.http = HttpRequest(
            log=self.log,
            proxy=self.proxy,
            user_agent=self.user_agent,
            tgWebData=self.web_app_query,
            account_name=self.account_name,
        )

        ref_link = None
        if self.isPyrogram and self.tgAccount is not None and self.tgAccount.NewStart:
            ref_link = (
                f"https://major.bot/?tgWebAppStartParam={self.tgAccount.ReferralToken}"
            )

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

        tasks = Tasks(
            log=self.log, httpRequest=self.http, account_name=self.account_name
        )

        self.log.info(f"<cyan>{self.account_name}</cyan><g> | 📋 Getting tasks ...</g>")
        all_tasks = tasks.get_tasks(is_daily=False)

        self.log.info(
            f"<cyan>{self.account_name}</cyan><g> | 📋 Getting daily tasks ...</g>"
        )
        daily_tasks = tasks.get_tasks(is_daily=True)
