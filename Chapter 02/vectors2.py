def add (*vectors):
    return (sum(v[0] for v in vectors), sum(v[1] for v in vectors))

def translate(translation, vectors):
    return [add(translation, v) for v in vectors]
