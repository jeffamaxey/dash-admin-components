import dash_html_components as html
from dash.development._py_components_generation import (
    filter_props,
    js_to_py_type,
    reorder_props,
)


def ApiDoc(component_metadata, component_name=None):
    component_props = component_metadata.get("props", {})
    return html.Div(
        ArgumentsList(component_props, component_name),
        className="api-documentation",
    )


def ArgumentsList(component_props, component_name):
    if component_name is not None:
        heading = f"Keyword arguments for {component_name}"
    else:
        heading = "Keyword arguments"
    component_props = reorder_props(filter_props(component_props))
    if arguments := [
        Argument(name, metadata) for name, metadata in component_props.items()
    ]:
        return [
            html.H4(heading, className="mt-5 mb-2"),
            html.Ul(arguments, className="list-unstyled"),
        ]
    else:
        return []


def Argument(argument_name, argument_metadata):
    description = argument_metadata.get("description", "")
    required = "" if argument_metadata.get("required", False) else ", optional"
    argument_type = argument_metadata.get("type", {})
    argument_type = js_to_py_type(argument_type)
    type_string = "" if argument_type is None else f" ({argument_type}{required})"
    return html.Li(
        [html.Code(argument_name), html.I(type_string), ": ", description]
    )
