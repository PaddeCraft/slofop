from slofop import *
import threading
import time

log = Logger(
    level=LoggingLevel.DEBUG,
    logfile_path="./test.log",
)

log.debug(locals())
log.info("Info")
log.warn("Warn")
log.error("Error")
log.critical("Critical")


def testThread():
    for i in range(4):
        log.debug("Running in " + threading.current_thread().name)
        log.info("Thread running time " + str(i + 1))
        time.sleep(1)


threading.Thread(target=testThread).start()
