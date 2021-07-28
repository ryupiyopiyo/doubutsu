import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)


class Horu(JoycontrolPlugin):
    async def run(self):
        logger.info('================HORU==================')

        while True:

            await self.left_stick('up')
            await self.wait(1.0)

            await self.button_push('a')
            await self.wait(1.0)
