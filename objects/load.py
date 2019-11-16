
from importlib import import_module, reload

def run_example(example_name, your_locals=None):
    module = reload(import_module('ex_{}'.format(example_name)))
    if your_locals is None:
        return
    loaded = {
        var_name: var_val
        for var_name, var_val
        in module.__dict__.items()
        if not var_name.startswith('__')
    }
    your_locals.update(loaded)
