import logging
import numpy # dummy import

logging.basicConfig(filename="log.txt",
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

print('Start from python!')
logging.info("starting test")
logger = logging.getLogger('log')
print('Done from python!')

# sudo  docker run --name test_python -it test_python_app:1.0 /bin/bash