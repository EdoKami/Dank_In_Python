class Func:

    @staticmethod
    def animate_text(text, delay, end_char='\n'):
        import time as t

        lines = text.split('\n')
        for line in lines:
            line = line.rstrip()
            for char in line:
                t.sleep(delay)
                print(char, end='')
            print(end=end_char)

    @staticmethod
    def create(y):
        open(y, "a")

    @staticmethod
    def clear_cmd():
        import os
        os.system('cls')

    @staticmethod
    def getip():
        import socket
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)

        print("Hostname: ", hostname)
        print("IPv4 Address: ", ip_address)

    @staticmethod
    def read_file(file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            content = ''.join(lines)
            return content

    @staticmethod
    def write_file(file_name, content):
        with open(file_name, "w") as f:
            w = f.write(content)
            return w

    @staticmethod
    def append_file(file_name, content):
        with open(file_name, "a") as f:
            a = f.write(content)
            return a

    @staticmethod
    def count_words(text):
        words = text.split()
        return len(words)

    @staticmethod
    def reverse_text(text):
        rev = text[::-1]
        return rev

    @staticmethod
    def cap_first_letter(text):
        return text.capitalize()
