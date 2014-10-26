'''
set basic configuration
'''
from rider import conf
from os.path import dirname

conf.BASE_DIR = dirname(__file__)

'''
load custom configuration
'''
try:
    import conf
except ImportError:
    pass

'''
load routes or views
'''
import routes


'''
import WSGI object application
'''
from rider import application
