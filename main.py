import subprocess
import threading


class Overclocking:
    def __init__(self):
        self._powerlimit_watts = 152
        self._funs_speed = 100
        # looking for Nvidia cards
        self.nvidia_cards = int(subprocess.check_output('nvidia-smi -L | wc -l', shell=True).decode())
        print(f'{self.nvidia_cards} NVIDIA cards found.')

    def set_powerlimit(self):
        for gpu in range(0, self.nvidia_cards):
            _thread = threading.Thread(target=self._threaded_set_powerlimit, args=(gpu,), daemon=False)
            _thread.start()

    def _threaded_set_powerlimit(self, gpu):
        print(f'Start to set powerlimit for card {gpu}')
        out = subprocess.check_output(f'sudo nvidia-smi -i {gpu} -pm 1', shell=True).decode()
        print(out)
        out = subprocess.check_output(f'sudo nvidia-smi -i {gpu} -pl {self._powerlimit_watts}', shell=True).decode()
        print(out)

    def set_funs_speed(self):
        for gpu in range(0, self.nvidia_cards):
            print(f'Start to set fun speed for card {gpu}')
            out = subprocess.check_output(f'nvidia-settings -a "[gpu:{gpu}]/GPUFanControlState=1"', shell=True).decode()
            print(out)
            out = subprocess.check_output(f'nvidia-settings -a "[fan:{gpu}]/GPUTargetFanSpeed={self._funs_speed}"',
                                          shell=True).decode()
            print(out)

if __name__ == '__main__':
    obj = Overclocking()
    obj.set_powerlimit()
    obj.set_funs_speed()
