# < (c) 2021 @kaif-00z >

from bot import dB


def is_approved(id):
    x = eval(dB.get("APPROVE_USERS") or "[]")
    if id in x:
        return True
    return False


def add_approve(id):
    x = eval(dB.get("APPROVE_USERS") or "[]")
    if id not in x:
        x.append(id)
        dB.set("APPROVE_USERS", str(x))


def rem_approve(id):
    x = eval(dB.get("APPROVE_USERS") or "[]")
    if id in x:
        x.remove(id)
        dB.set("APPROVE_USERS", str(x))
