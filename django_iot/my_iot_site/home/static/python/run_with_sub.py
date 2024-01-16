import subprocess


def main(topic, payload):
    arg_lst = ["python3", "test_system.py", "--topic", f"{topic}", "--payload", f"{payload}"]
    with subprocess.Popen(arg_lst, stderr=subprocess.PIPE, stdout=subprocess.PIPE) as process:
        stdout, stderr = process.communicate()
        print(f"STDOUT: {stdout}")
        print(f"STDERR: {stderr}")


if __name__ == "__main__":
    main(topic="living_room", payload="OFF")
