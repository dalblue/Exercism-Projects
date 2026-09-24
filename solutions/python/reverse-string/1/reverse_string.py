def reverse(text):
    backwards=""
    for e in text[-1::-1]:
        backwards+=e
    return backwards
