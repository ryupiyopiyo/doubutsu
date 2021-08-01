import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)


class BuyRemakeKit(JoycontrolPlugin):
    async def run(self):
        logger.info('リメイクキットを買いまくる！')

        await self.button_push('a')
        await self.wait(0.7)

        await self.button_push('a')
        await self.wait(2.0)
