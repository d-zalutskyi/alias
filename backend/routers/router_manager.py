from logger import Logger

logger = Logger.setup_logger(__name__)

class RouterManager:

    @classmethod
    async def check_health(cls) -> str:
        return "I am alive"
