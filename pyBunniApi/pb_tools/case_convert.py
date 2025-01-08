import re


def to_snake_case(name: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()


def to_camel_case(name: str) -> str:
    components = name.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
