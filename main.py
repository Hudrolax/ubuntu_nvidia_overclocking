import subprocess
import threading


class Overclocking:
    def __init__(self):
        self.powerlimit_watts = 152
        # looking for Nvidia cards
        self.nvidia_cards = int(subprocess.check_output('nvidia-smi -L | wc -l', shell=True).decode())
        print(f'{self.nvidia_cards} NVIDIA cards found.')

    def set_powerlimit(self):
        for card in range(0, 12):
            _thread = threading.Thread(target=self._threaded_set_powerlimit, args=(card,), daemon=False)
            _thread.start()

    def _threaded_set_powerlimit(self, card):
        print(f'Start to set powerlimit for card {card}')
        out = subprocess.check_output(f'sudo nvidia-smi -i {card} -pm 1', shell=True).decode()
        print(out)
        out = subprocess.check_output(f'sudo nvidia-smi -i {card} -pl {self.powerlimit_watts}', shell=True).decode()
        print(out)

if __name__ == '__main__':
    obj = Overclocking()
    obj.set_powerlimit()
