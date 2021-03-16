# -*- coding: gbk -*-
# A multi thread template
# Author: YoungC
import os
import time
import threading
import subprocess
from collections import Iterator
class JiuWei_Fox():
    def __init__(self, number_of_the_tails):
        self.number_of_the_tails = number_of_the_tails
        self.bell = None
        self.tails = []
        self.snap_time = 30
        self.help = "青丘之山，有兽焉，其状如狐而九尾。\n"
        self.help += "JiuWei Fox is a kind of fantasy creatures in Chinese legend, which has nine tails. "
        self.help += "The tales of JiuWei Fox have spreat over the east Asia, for example, Japanese call it Gumiho.\n"
        self.help += "Now, you have one as helpful partner! "
        self.help += "You can (ring) the (bell) to motivate its (tail)s to do the (action). And the JiuWei Fox will howl the result.\n"
    def howl(self, *args):
        print(*args)
    def action(self, *args):
        print("Not impletement yet.")
        self.howl(*args)
    def comb_the_tail(self):
        for tail in self.tails:
            if not tail.is_alive():
                self.tails.remove(tail)
        return len(self.tails)
    def set_the_bell(self, bell):
        if isinstance(bell, Iterator):
            self.bell = bell
            return True
        else:
            print("Broken Bell !")
            return False
    def ring(self):
        self.comb_the_tail()
        if len(self.tails) >= self.number_of_the_tails:
            print("All tails are busy now." )
            return 1
        try:
            sound = next(self.bell)
        except StopIteration:
            return -1
        tail = threading.Thread(target=self.action, args=(sound,))
        self.tails.append(tail)
        tail.start()
        return 0
    def run_fox_run(self):
        if not self.bell:
            print("Give me the bell!")
            return False
        while True:
            ret_code = self.ring()
            if ret_code == -1:
                break
            elif ret_code == 1:
                time.sleep(self.snap_time)
        print("Waiting for all tails' return.")
        while True:
            ret_code = self.comb_the_tail()
            if ret_code == 0:
                break
            else:
                time.sleep(self.snap_time)
        print("All is done!")

#=========#
# Testing #
#=========#
if __name__ == "__main__":
    def the_bell(path):
        for _root, _dir, _files in os.walk(path):
            for f in _files:
                ida_pkl_file = os.path.join(_root, f)
                yield ida_pkl_file
    class My_Fox(JiuWei_Fox):
        def action(self, *args):
            save_name = args[0]
            p = subprocess.Popen("python test.py %s" % save_name, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            ret_code = p.wait()
            print("parsing %s: Done[%d]" % (save_name, ret_code))
            print(p.stdout.readlines())
            return ret_code
    my_fox = My_Fox(20)
    my_fox.set_the_bell(the_bell("../"))
    my_fox.run_fox_run()
