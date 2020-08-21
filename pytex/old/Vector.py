
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/Vector.ipynb
from pytex import Var
from pytex.helpers import varArgFunc
class Vector(Var):
    def __init__(self, name):
        super().__init__(r"\vec{\mathbf{" + name +"}}")

def makeVector(*args):
    return varArgFunc(lambda arg: arg if isinstance(arg, Vector) else Vector(str(arg)), *args)