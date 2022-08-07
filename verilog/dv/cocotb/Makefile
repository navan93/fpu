# Makefile

COMPILE_ARGS =  -f filelist_rtl.f

# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# VERILOG_SOURCES += $(PWD)/my_design.sv
# VERILOG_SOURCES += ../../rtl/fpu_sp_top.sv \
# 									 ../../rtl/fpu_sp_add.sv \
# 									 ../../rtl/fpu_sp_mul.sv \
# 									 ../../rtl/fpu_sp_div.sv \
# 									 ../../rtl/fpu_sp_f2i.sv \
# 									 ../../rtl/fpu_sp_i2f.sv \
# 									 ../../rtl/fpu_dp_add.sv \
# 									 ../../rtl/fpu_dp_mul.sv \
# 									 ../../rtl/fpu_dp_div.sv


# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = fpu_sp_top

# MODULE is the basename of the Python test file
MODULE = test_fpu_sp_top

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim