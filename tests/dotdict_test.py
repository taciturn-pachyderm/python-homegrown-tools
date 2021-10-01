from src.dotdict import *
 
d=None


def test_empty_init():
    global d
    d = dotdict()
    
    assert isinstance(d, dotdict)
    assert d.__str__() == '{}'
    

def test_copy_init():
    global d
    d = dotdict( { "a": 3, "b": "string", "c": False } )
    
    assert isinstance(d, dotdict)
    assert d.a == 3
    assert d.b == "string"
    assert d.c == False
    assert list(d.keys()) == ["a", "b", "c"]
    
    
def test_nested_copy_init():
    global d
    d = dotdict(
        {
            "c": [
                {"a":5},
                {"b":[
                    {"a":4}
                ]}
            ],
            "d": [1,2,3]
        }
    )
    
    assert isinstance(d, dotdict)
    assert type(d.c) == list
    assert d.c[0].a == 5
    assert d.c[1].b[0].a == 4
    assert d.d == [1,2,3]
    assert list(d.keys()) == ["c","d"]
    
    d = dotdict([[[[{"a":3}]]]])
    assert d[0][0][0][0].a == 3
    
    
def test_dot_get_set():
    global d
    d = dotdict()
    d.e = 4
    d.f = "5"
    d.g = True
    d.h = { "a": 3, "b": "string", "c": False }
    d.i = d.e
    
    assert type(d.h) == dotdict
    assert d.e == d.i == 4
    assert d.f == "5"
    assert d.g == True


# def test_nested_insert():
#     global d
#     d = dotdict()
#     d.j.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p = 3
    
#     assert d.j.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p == 3
#     assert type(d.j.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o) == dotdict 
#     assert type(d.j) == dotdict 
