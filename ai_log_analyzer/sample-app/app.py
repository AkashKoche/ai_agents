import time
import random
import logging

logging.basicConfig(
    filename="/var/log/app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelsname)s %(message)s"
)

while True:
    r = random.randint(1, 100)

    if r < 10:
        logging.error("OutOfMemoryError: Java heap space")
    elif r < 20:
        logging.error("Connection timeout to database")
    elif r < 30:
        logging.warning("CPU usage above 85%")
    else:
        logging.info("Requested processed successfully")

    time.sleep(2)
