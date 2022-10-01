import yaml, json


def _yaml_load(y):
    return yaml.load(y, Loader=yaml.loader.SafeLoader)


def yaml2dict(yaml_source):
    """convert file path or buffer containing YAML-compliant serialized string object 
        OR the literal string itself to python dictionary object"""
    
    try:    # try as file-path or file-buffer
        return _yaml_load(
            open(yaml_source) if isinstance(yaml_source, str)
            else yaml_source
        )
    except FileNotFoundError: # try argument as a literal string
        return _yaml_load(yaml_source)
    

def json2dict(json_source):
    """convert file path or buffer containing JSON-compliant serialized string object 
        OR the literal string itself to python dictionary object"""
    try:    # try as file-path or file-buffer
        return json.load(
            open(json_source) if isinstance(json_source, str)
            else json_source
        )
    except FileNotFoundError: # try argument as a literal string
        return json.loads(json_source)
 
 
def yaml2json(*yaml_sources, **kwargs):
    """convert YAML-compliant serialized string object to JSON-compliant serialized string object"""
    
    json_out = [yaml2dict(yaml_source) for yaml_source in yaml_sources]
    
    if len(json_out) == 1:
        json_out = json_out[0]
    
    return json.dumps(
        json_out,
        **kwargs
    )


def dict2yaml(d):
    return yaml.dump(d)

    
def json2yaml(*json_sources):
    """
    convert a list containing JSON-compliant serialized strings,
    or file-paths/file-buffers containing JSON-compliant serialized strings
    to YAML-compliant serialized string object
    """
    
    yaml_out = [dict2yaml(json2dict(json_source)) for json_source in json_sources]
    
    return "---\n".join(yaml_out)