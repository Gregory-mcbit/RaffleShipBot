from warn import warns
from admin_bot import main
import asyncio


if __name__ == "__main__":
    warns.ignore()  # suppress all warnings
    asyncio.run(main.main())  # start bot polling
