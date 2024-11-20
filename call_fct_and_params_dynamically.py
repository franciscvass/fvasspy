import inspect

def my_function(a, b):
    print(f"a: {a}, b: {b}")

def my_function1(c, d):
    print(f"c: {c}, d: {d}")

def my_function2(e, f, g):
    print(f"e: {e}, f: {f}, g: {g}")

param_list = [[10,20,100],[30,40,200],[50,60,70]]

fct_list = {'my_function':my_function,'my_function1':my_function1,'my_function2':my_function2}

for f in ["my_function","my_function1","my_function2"]:
    sig = inspect.signature(fct_list[f])
    dyn_args = {}
    for p in param_list:
        i = 0
        for fct_param in sig.parameters:
            dyn_args[fct_param]=p[i]
            i = i+1
        fct_list[f](**dyn_args)
