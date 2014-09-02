
def import_module(module):
    __import__(module, globals(), locals(), [], 0)

def import_object(dot_path):
    dot_path_split = dot_path.split('.')
    module_name = '.'.join(dot_path_split[0:-1])
    object_name = dot_path_split[-1]
    module = __import__(module_name, globals(), locals(), [module_name], 0)
    return getattr(module, object_name)
