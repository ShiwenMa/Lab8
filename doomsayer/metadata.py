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

  # If IP addresses have been provided in the event, check if the source IP is a-ok.
  if 'authorised-ips' in event:
    if 'source-ip' in event and not event['source-ip'] in event['authorised-ips']:
      raise Exception( 'Unauthorised.' )

  # If IP addresses have been provided in an environment variable, check if the source IP is a-ok.
  if 'AUTHORISED_IPS' in os.environ:
    authorised_ips = os.environ['AUTHORISED_IPS'].split( ',' )
    if 'source-ip' in event and not event['source-ip'] in authorised_ips:
      raise Exception( 'Unauthorised.' )

  ec2 = boto3.client( 'ec2', region_name = event['region'] )

  # Start or stop the requested instance(s).
  if 'start' == event['action']:
    ec2.start_instances( InstanceIds = event['instances'] )
  elif 'stop' == event['action']:
    ec2.stop_instances( InstanceIds = event['instances'] )

def count_instances(ec2):
    total_instances = 0
    instances = ec2.instances.filter(          Filters=[
              {
                  'Name': 'instance-state-name',
                  'Values': [
                      'running',
                  ]
              },
        ])
    for _ in instances:
        total_instances += 1
    return total_instances