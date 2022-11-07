# objects[0] : 바닥계층
# objects[1] : 상위계층
objects = [[], []]

def add_object(o, depth):
    objects[depth].append(o)

def all_objects():
    for layer in objects:
        for o in layer:
            yield o

def remove_object(o, depth):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            del o
            break

def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()