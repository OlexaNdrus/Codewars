def isValidWalk(walk):
    if walk.count('n')==walk.count('s') and walk.count('w')==walk.count('e') and len(walk)==10:
        return True
    return False