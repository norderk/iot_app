import subprocess

def main(topic, payload):
    arg_lst = ["python3", "test_system.py", "--topic", f"{topic}", "--payload", f"{payload}"]
    subprocess.Popen(arg_lst, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

if __name__ == '__main__':
    topic = "living_room"
    payload = "OFF"
    main(topic, payload)
