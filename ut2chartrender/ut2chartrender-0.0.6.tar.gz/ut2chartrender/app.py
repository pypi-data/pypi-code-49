from .chart import generate_highchart
from .renderer import __render_chart


def generate_chart(options, datasets, ttw=1):
    xml = __render_chart(generate_highchart(options, datasets), ttw=ttw)
    return xml
