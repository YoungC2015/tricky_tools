# auto set environment to bashrc
# Test passed, 2019-01-16
import os, sys

def inform():
    print ("Usage: this.py [bashrc_file]")
    print ("using default ~/.bashrc")
    return "~/.bashrc"

if __name__ == "__main__":
    try:
        import readline
    except ImportError:
        print ("You need pip install readline(or pyreadline on windows)")
    
    bashrc = inform() if len(sys.argv) < 2 else sys.argv[1]
    os.system('echo "export PYTHONSTARTUP=\\"`pwd`/python_auto_complete.py\\"" >> %s' % bashrc)
    #os.system('bash source %s' % bashrc)
