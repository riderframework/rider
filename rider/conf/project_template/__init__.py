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
try:
    import routes
except ImportError:
    try:
        import views
    except ImportError:
        raise ImportError('Cannot import routes or views.')

'''
import WSGI object application
'''
from rider import application
