import time

delay = 0.1

def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='='):
    percent = ('{0:.' + str(decimals) + 'f}').format(100*(iteration/float(total)))
    filled = int(length*iteration//total)
    bar = fill*filled + '-'*(length - filled)

    print(f'\r{prefix} [{bar}] {percent}% {suffix}', end='\r')
    if iteration == total:
        print()

items = list(range(0, 50))
l = len(items)

loadbar(0, l, prefix='Progress:', suffix='Complete', length=l)
for i, item in enumerate(items):
    time.sleep(delay)
    loadbar(i + 1, l, prefix='Progress:', suffix='Complete', length=l)
