from jinja2 import Environment, FileSystemLoader
from rider import conf
from rider.routes import url
from os import path


environment = Environment(
    loader=FileSystemLoader(path.join(conf.BASE_DIR, conf.templates.PATH)),
)
environment.globals['url'] = url

TEMPLATE_CACHE = {}


def render(template_name, context={}):
    if template_name in TEMPLATE_CACHE:
        template = TEMPLATE_CACHE[template_name]
    else:
        template = TEMPLATE_CACHE.setdefault(template_name, environment.get_or_select_template(template_name))
    return template.render(context)
