import struct

CMD_FPU_SP_ADD  = 0b0001 # Single Precision (32 bit) Adder
CMD_FPU_SP_MUL  = 0b0010 # Single Precision (32 bit) Multipler
CMD_FPU_SP_DIV  = 0b0011 # Single Precision (32 bit) Divider
CMD_FPU_SP_F2I  = 0b0100 # Single Precision (32 bit) Float to Integer
CMD_FPU_SP_I2F  = 0b0101 # Single Precision (32 bit) Integer to Float
CMD_FPU_DP_ADD  = 0b1001 # Double Precision (64 bit) Adder
CMD_FPU_DP_MUL  = 0b1010 # Double Precision (64 bit) Multipler
CMD_FPU_DP_DIV  = 0b1011 # Double Precision (64 bit) Divider

def bin_to_float32(val):
    return struct.unpack("<f", struct.pack("<I", val))[0]

def float32_to_bin(val):
    return struct.unpack('i',struct.pack('f',val))[0]