#Module to set up polling of instance metadata for the termination of a spot instance
import logging
import logging.handlers
import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%d-%m %H:%M',
    filename='doomsayer.log'
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def poll_instance_metadata():
    r = requests.get("http://169.254.169.254/latest/meta-data/spot/termination-time")
    logging.info(r.content)
    return r.status_code < 400
