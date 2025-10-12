# test_my_design.py (simple)

import cocotb
from cocotb.triggers import Timer, RisingEdge, ClockCycles, FallingEdge
from cocotb.clock import Clock
from fpu_utils import *
from fpu_sp_model import fpu_sp_model
import pprint as pp

async def powerup_dut(dut):
    """Try accessing the design."""

    # "Clock" is a built in class for toggling a clock signal
    cocotb.start_soon(Clock(dut.clk, 10, units='ns').start())

    dut.rst_n.value = 0
    dut.cmd.value = 0
    dut.din1.value = 0
    dut.din2.value = 0
    dut.dval.value = 0
    await Timer(100, units="ns")
    dut.rst_n.value = 1

@cocotb.test()
async def my_first_test(dut):
    """Try accessing the design."""

    # "Clock" is a built in class for toggling a clock signal
    cocotb.start_soon(Clock(dut.clk, 10, units='ns').start())

    dut.rst_n.value = 0
    dut.cmd.value = 0
    dut.din1.value = 0
    dut.din2.value = 0
    dut.dval.value = 0
    await Timer(100, units="ns")
    dut.rst_n.value = 1

    await ClockCycles(dut.clk, 10)

    dut.cmd.value = CMD_FPU_SP_ADD
    dut.din1.value = float2bin(0.5) #0x3f000000
    dut.din2.value = float2bin(1.0) #0x3fc00000
    dut.dval.value = 1
    await ClockCycles(dut.clk, 1)
    dut.dval.value = 0
    await FallingEdge(dut.rdy)

    result = bin2float(dut.result.value)
    dut._log.info("Result is %s", result)
    assert result == 1.5, "Adder failure"

@cocotb.test()
async def inspect_design(dut):
    await powerup_dut(dut)

    # print(dir(dut))
    # print(dir(dut.cmd))
    pp.pprint(dir(dut.u_sp_add))
    pp.pprint((dut.u_sp_add._name))
    pp.pprint((dut.u_sp_add._type))
    pp.pprint((dut.u_sp_add._path))


    # print("output logic [31:0]   result ", type(dut.result))
    # print("logic        sp_add_rdy ", type(dut.sp_add_rdy))
    # print("fpu_sp_add  u_sp_add ", type(dut.u_sp_add))


