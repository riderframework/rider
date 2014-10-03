from rider.utils import import_module


def configure(work_dir, conf_module):
    globals()['WORK_DIR'] = work_dir
    conf = import_module(conf_module)
    for submodule_name in ('templates', ):
        submodule = __import__('%s.%s' % (conf_module, submodule_name), {}, {}, [submodule_name])
        submodule_conf = __import__(submodule_name, globals())
        for var in dir(submodule_conf):
            if not var.startswith('__') and var in dir(submodule):
                setattr(submodule_conf, var, getattr(submodule, var))


