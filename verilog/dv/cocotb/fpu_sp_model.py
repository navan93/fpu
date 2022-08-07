# Model for single precision 32-bit FPU

from fpu_utils import *

def fpu_sp_add(in1, in2):
  pass

def fpu_sp_div(in1, in2):
  pass

def fpu_sp_mul(in1, in2):
  pass

def fpu_sp_f2i(in1):
  pass

def fpu_sp_i2f(in1):
  pass

def fpu_sp_model(cmd, in1, in2=None):
  if cmd == CMD_FPU_DP_ADD:
    return fpu_sp_add(in1, in2)
  elif cmd == CMD_FPU_DP_DIV:
    return fpu_sp_div(in1, in2)
  elif cmd == CMD_FPU_DP_MUL:
    return fpu_sp_mul(in1, in2)
  elif cmd == CMD_FPU_SP_F2I:
    return fpu_sp_f2i(in1)
  elif cmd == CMD_FPU_SP_I2F:
    return fpu_sp_i2f(in1)
  else:
    raise Exception("Invalid FPU Operation")