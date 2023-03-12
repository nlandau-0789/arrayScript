import inspect, pprint

def var_name(var):
    lcls = inspect.stack()[2][0].f_locals
    for name in lcls:
        if id(var) == id(lcls[name]):
            return name
    return None

class bundle(dict):
    def __getattr__(self, name):
        if name in self: return self[name]
        return "Unknown"

    def __iadd__(self, other):
        self[var_name(other)] = other
        return self
    
    def __add__(self, other):
        self[var_name(other)] = other
        return self

    def __repr__(self):
        res = "bundle :\n"
        for key, val in self.items():
            res += f"{key.upper().center(92).replace(' ', '=')}\n{pprint.pformat(val)}\n\n"
        return res