import time
from plugins import plugin
from importlib import reload
while 1:
    reload(plugin)
    plugin.crack()
    time.sleep(1)
