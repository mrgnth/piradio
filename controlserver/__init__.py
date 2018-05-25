import socket
from time import sleep
from subprocess import check_output, Popen, PIPE, CalledProcessError


class VLCController:
    '''
    This class makes sure an instance of vlc is running and listening to
    remote control commands on the host:port specified in the respective
    constants. It is then possible to control the VLC instance via the
    object methods.
    Inspired by Marios Zindilis:
    https://zindilis.com/blog/2016/10/23/control-vlc-with-python.html
    because the official Python VLC bindings are too much of a hassle in
    this case.
    '''
    def __init__(self):
        self.HOST = 'localhost'
        self.PORT = 8888

    def start(self):
        proc_started = False
        while not self.__vlc_running:
            if not proc_started:
                Popen(f'vlc -I rc --rc-host {self.HOST}:{self.PORT}'.split(),
                      stdout=PIPE, stdin=PIPE, stderr=PIPE)
                proc_started = True
            sleep(1)
        self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SOCK.connect((self.HOST, self.PORT))

    @property
    def __vlc_running(self):
        exit_code = 0
        output = ''
        vlc_procs = []
        try:
            output = check_output('ps aux'.split())
            vlc_procs = [f.decode() for f in output.split(b'\n') if b'vlc' in f]
        except CalledProcessError as e:
            exit_code = e.returncode
            output = e.output
            print(f'Oh no, ERROR, ERROR! {exit_code}: {output}')

        for p in vlc_procs:
            if f'{self.HOST}:{self.PORT}' in p:
                return True
        return False

    def __send_command(self, cmd):
        '''Prepare a command and send it to VLC'''
        if not cmd.endswith('\n'):
            cmd = cmd + '\n'
        cmd = cmd.encode()
        self.SOCK.sendall(cmd)

    def pause(self):
        if not self.__vlc_running:
            self.start()
        self.__send_command('pause')

    def play(self):
        if not self.__vlc_running:
            self.start()
        self.__send_command('play')

    def stop(self):
        if not self.__vlc_running:
            self.start()
        self.__send_command('stop')

    def prev(self):
        if not self.__vlc_running:
            self.start()
        self.__send_command('prev')

    def next(self):
        if not self.__vlc_running:
            self.start()
        self.__send_command('next')

    def add(self, path):
        if not self.__vlc_running:
            self.start()
        self.__send_command(f'add {path}')

    def enqueue(self, path):
        if not self.__vlc_running:
            self.start()
        self.__send_command(f'enqueue {path}')

    def clear(self):
        if not self.__vlc_running:
            self.start()
        self.__send_command('clear')

    def shutdown(self):
        if self.__vlc_running:
            self.__send_command('shutdown')


vlc_controller = VLCController()
vlc_controller.start()
