import asyncio
from service.processor import MessageProcessor

class NutsSubscriber:
    def __init__(self):
        self.processor = MessageProcessor()

    async def listen(self):
        while True:
            msg = await self.simulate_message()
            print(f"Received: {msg}")
            self.processor.validate_and_save(msg)

    async def simulate_message(self):
        await asyncio.sleep(2)
        return "Test message from Nuts"

    def shutdown(self):
        self.processor.shutdown()

