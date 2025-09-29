from utils.logger import loading, success
from time import sleep


with loading("Seeding Starts..."):
    import seeders.acheteur as _
    sleep(2.5)

success("Seeding done" + "\n" * 2)
