from src.yaml2json import *
import sys, os, shutil


def self_cleaning_tmpdir(f):
    def F(tmpdir):
        f(tmpdir)
        shutil.rmtree(tmpdir.strpath)
    return F
        

def test_dict_to_yaml():
    d = {"a":3,"b":[1,2,3]}
    assert dict2yaml(d) == 'a: 3\nb:\n- 1\n- 2\n- 3\n'
    

@self_cleaning_tmpdir
def test_json_to_yaml(tmpdir):
    test_json_string = '{"a":3,"b":[1,2,3]}'
    target_yaml_string = 'a: 3\nb:\n- 1\n- 2\n- 3\n'
    
    test_json_file = tmpdir + '/test.json'
    test_json_file.write(test_json_string)
    
    # test stringified JSON
    assert json2yaml(test_json_string) == target_yaml_string
    
    # test JSON file containing stringified JSON
    assert json2yaml(test_json_file.strpath) == target_yaml_string
    
    
@self_cleaning_tmpdir
def test_yaml_to_dict(tmpdir):
    test_yaml_string = "a: 3\nb:\n- 1\n- 2\n- 3\n"
    target_json_string = '{"a": 3, "b": [1, 2, 3]}'
    
    test_yaml_file = tmpdir + '/test.yaml'
    test_yaml_file.write(test_yaml_string)
    
    # test stringified YAML
    assert yaml2json(test_yaml_string) == target_json_string
    assert yaml2json(test_yaml_string, separators=[',',':']) == target_json_string.replace(' ','')
    
    # test YAML file containing stringified YAML
    assert yaml2json(test_yaml_file.strpath) == target_json_string
