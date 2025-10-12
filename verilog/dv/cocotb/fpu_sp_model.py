# Model for single precision 32-bit FPU

from fpu_utils import *
import numpy as np

def fpu_sp_add(in1, in2):
  a = bin2float(in1)
  b = bin2float(in2)
  c = np.sum([a, b], dtype=np.float32)
  c = float2bin(c)
  return c

def fpu_sp_div(in1, in2):
  a = bin2float(in1)
  b = bin2float(in2)
  c = np.divide(a, b, dtype=np.float32)
  c = float2bin(c)
  return c

def fpu_sp_mul(in1, in2):
  a = bin2float(in1)
  b = bin2float(in2)
  c = np.multiply(a, b, dtype=np.float32)
  c = float2bin(c)
  return c

def fpu_sp_f2i(in1):
  pass

def fpu_sp_i2f(in1):
  pass

def fpu_sp_fmadd(in1, in2, in3):
  a = bin2float(in1)
  b = bin2float(in2)
  c = bin2float(in3)
  res = np.multiply(a, b, dtype=np.float32)
  res = np.sum([res, c], dtype=np.float32)
  return res

def fpu_sp_fmsub(in1, in2, in3):
  a = bin2float(in1)
  b = bin2float(in2)
  c = bin2float(in3)
  res = np.multiply(a, b, dtype=np.float32)
  res = np.subtract(res, c, dtype=np.float32)
  return res

def fpu_sp_fnmsub(in1, in2, in3):
  a = bin2float(in1)
  b = bin2float(in2)
  c = bin2float(in3)
  res = np.multiply(a, b, dtype=np.float32)
  res = np.subtract(c ,res, dtype=np.float32)
  return res

def fpu_sp_fnmadd(in1, in2, in3):
  a = bin2float(in1)
  b = bin2float(in2)
  c = bin2float(in3)
  res = np.multiply(a, b, dtype=np.float32)
  res = np.subtract(c ,res, dtype=np.float32)
  return res

def fpu_sp_model(cmd, in1, in2=None, in3=None):
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

def main():
  a = float2bin(0.1)
  b = float2bin(0.2)
  res = fpu_sp_div(a, b)
  print(hex(res))
  print(bin2float(res))


if __name__ == "__main__":
  main()