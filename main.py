import asyncio
from api.subscriber import NutsSubscriber

async def main():
    subscriber = NutsSubscriber()
    try:
        await subscriber.listen()
    except KeyboardInterrupt:
        print("Shutting down...")
        subscriber.shutdown()

if __name__ == "__main__":
    asyncio.run(main())

