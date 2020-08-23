import subprocess
import threading


class Overclocking:
    def __init__(self):
        # looking for Nvidia cards
        lspci_out = subprocess.check_output('lspci | grep NVIDIA', shell=True).decode().split('\n')
        self.nvidia_cards = []
        for line in lspci_out:
            if 'NVIDIA' in line:
                self.nvidia_cards.append(line)
        print('Founded NVIDIA cards:')
        for card in enumerate(self.nvidia_cards):
            print(card)

        # # prepare system for overclocking
        # display = subprocess.check_output('export DISPLAY=:0', shell=True)
        # display = subprocess.check_output('export XAUTHORITY=/var/run/lightdm/root/:0', shell=True)
        # display = subprocess.check_output('sudo xhost +', shell=True).decode()
        # print(display)
        # if display.lower().find('unable to open display') > -1:
        #     print('error open display port')
        #     exit()

    def set_powerlimit(self):
        for card in enumerate(self.nvidia_cards):
            _thread = threading.Thread(target=self._threaded_set_powerlimit, args=(card[0],), daemon=False)
            _thread.start()

    def _threaded_set_powerlimit(self, card):
        print(f'Start to set powerlimit for card {card}')
        subprocess.check_output(f'sudo nvidia-smi -i {card} -pm 1', shell=True)
        subprocess.check_output(f'sudo nvidia-smi -i {card} -pl 70', shell=True)
        print(f'powerlimit for card {card} set to 70%')

if __name__ == '__main__':
    obj = Overclocking()
    obj.set_powerlimit()
