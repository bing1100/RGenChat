import signal
TIMEOUT = 3 # number of seconds your want for timeout

def interrupted(signum, frame):
    "called when read times out"
    print 'interrupted!'
    raise Exception("Time is Up")

signal.signal(signal.SIGALRM, interrupted)

def minput():
    try:
            print 'You have 5 seconds to type in your stuff...'
            foo = raw_input()
            return foo
    except:
            # timeout
            return 

# set alarm
signal.alarm(TIMEOUT)
s = minput()
# disable the alarm after success
signal.alarm(0)
print 'You typed', s