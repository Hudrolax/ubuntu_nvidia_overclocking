import subprocess
import threading


class Overclocking:
    def __init__(self):
        self._POWERLIMIT_WATTS = 152
        self._FUNS_SPEED = 100
        self._MEM_CLOCK_OFFSET = 700
        self._CLOCK_OFFSET = -50
        # looking for Nvidia cards
        self.nvidia_cards = int(subprocess.check_output('nvidia-smi -L | wc -l', shell=True).decode())
        print(f'{self.nvidia_cards} NVIDIA cards found.')

    def set_powerlimit(self):
        for gpu in range(0, self.nvidia_cards):
            print(f'Start to set powerlimit for card {gpu}')
            out = subprocess.check_output(f'sudo nvidia-smi -i {gpu} -pm 1', shell=True).decode()
            out = subprocess.check_output(f'sudo nvidia-smi -i {gpu} -pl {self._POWERLIMIT_WATTS}', shell=True).decode()
            print(f'Powerlimit for GPU{gpu} setted to {self._POWERLIMIT_WATTS} W')

    def set_funs_speed(self):
        for gpu in range(0, self.nvidia_cards):
            print(f'Start to set fun speed for card {gpu}')
            out = subprocess.check_output(f'nvidia-settings -a "[gpu:{gpu}]/GPUFanControlState=1"', shell=True).decode()
            out = subprocess.check_output(f'nvidia-settings -a "[fan:{gpu}]/GPUTargetFanSpeed={self._FUNS_SPEED}"', shell=True).decode()
            print(f'Fun speed for GPU{gpu} setted to {self._FUNS_SPEED}%')

    def set_overclocking(self):
        for gpu in range(0, self.nvidia_cards):
            print(f'Overclocking card {gpu}...')
            out = subprocess.check_output(f'nvidia-settings -a "[gpu:{gpu}]/GPUMemoryTransferRateOffset[1]={self._MEM_CLOCK_OFFSET*2}', shell=True).decode()
            print(f'Memory clock offset for GPU{gpu} set to {self._MEM_CLOCK_OFFSET}')
            out = subprocess.check_output(f'nvidia-settings -a "[gpu:{gpu}]/GPUGraphicsClockOffset[1]={self._CLOCK_OFFSET}"', shell=True).decode()
            print(f'Core clock offset for GPU{gpu} set to {self._CLOCK_OFFSET}')

if __name__ == '__main__':
    obj = Overclocking()
    obj.set_powerlimit()
    obj.set_funs_speed()
    obj.set_overclocking()
    print('Done!')
