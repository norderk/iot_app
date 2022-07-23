import sys
import argparse
from lights import call_mqtt
from subprocess import run, PIPE


parser = argparse.ArgumentParser()
parser.add_argument('--topic', required=True, help='rootTopic/topic/uplink, ex: zigbee2mqtt/living_room/set')
parser.add_argument('--payload', required=True, help='ex: OFF/ON')
    
def run_mqtt(args):
    call_mqtt(topic=f"zigbee2mqtt/{args['topic']}/set", payload=args['payload'])

def main(): 
    args = vars(parser.parse_args())
    run_mqtt(args)

if __name__ == '__main__':
    main()
