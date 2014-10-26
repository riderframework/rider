from jinja2 import Environment, FileSystemLoader
from rider import conf
from rider.routes import url
from os import path


environment = Environment(
    loader=FileSystemLoader(path.join(conf.BASE_DIR, conf.templates.PATH)),
)
environment.globals['url'] = url


def render(template, context):
    template = environment.get_or_select_template(template)
    return template.render(context)
