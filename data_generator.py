import os
import random
import time

while True:
    os.system("""curl -i -XPOST 'http://172.18.0.4:8080/telegraf' --data-binary '{"id": 1, "pul": %d, "tension": %d}'""" % (
        random.randrange(40, 110), random.randrange(70, 130)))
    os.system("""curl -i -XPOST 'http://172.18.0.4:8080/telegraf' --data-binary '{"id": 2, "pul": %d, "tension": %d}'""" % (
        random.randrange(40, 110), random.randrange(70, 130)))
    os.system("""curl -i -XPOST 'http://172.18.0.4:8080/telegraf' --data-binary '{"id": 3, "pul": %d, "tension": %d}'""" % (
        random.randrange(40, 110), random.randrange(70, 130)))
    time.sleep(5)
