from jinja2 import Environment, FileSystemLoader
from rider import conf
from os import path

environment = Environment(
    loader=FileSystemLoader(path.join(conf.BASE_DIR, conf.templates.PATH))
)

def render(template, context):
    template = environment.get_or_select_template(template)
    return template.render({'conf': conf})
