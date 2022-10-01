class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    
    iter_map = {
        dict: lambda d: d.items,
        list: lambda l: l.enumerate
    }
    
    def __setattr__(self, key, value):
        if type(value) == dict:
            value = type(self)(value) # convert inserted dicts to dotdicts
            
        dict.__setitem__(self, key, value)
        
    # __getattr__ = dict.__getitem__
    def __getattr__(self, key):
        return dict.get(self, key, None)
            
    __delattr__ = dict.__delitem__
    
    def __new__(self, o={}):
        # for recursive dotdict() casting, return elementary types unmutated
        if type(o) == dict:
            return super().__new__(self,o)
        elif type(o) == list:
            return [ self(i) for i in o ]
        else:
            return o
                        
    
    def __init__(self, o={}):
        # try to recursively cast nested dicts to dotdicts
        try:
            for k,v in o.items():
                try:
                    for _k,_v in self.iter_map[type(v)](v):      
                        v[_k] = type(self)(_v)
                except:
                    v = type(self)(v)
                self[k] = v
        except:
            pass