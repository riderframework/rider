#!/usr/bin/env python

from rider.utils import commands
from rider.utils import server
import sys

if __name__ == "__main__":
    '''
    rider.py create [nazev_projektu]
    rider.py create [nazev_projektu].[nazev_aplikace]
    rider.py run project
    '''
    if len(sys.arg) == 3:
        if sys.arg[1] == 'create':
            commands.create(sys.arg[2])
        elif sys.arg[1] == 'run':
            server.run()


