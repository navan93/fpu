# test_my_design.py (simple)

import cocotb
from cocotb.triggers import Timer, RisingEdge, ClockCycles, FallingEdge
from cocotb.clock import Clock
from fpu_utils import *
from fpu_sp_model import fpu_sp_model


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
    dut.din1.value = float32_to_bin(0.5) #0x3f000000
    dut.din2.value = float32_to_bin(1.0) #0x3fc00000
    dut.dval.value = 1
    await ClockCycles(dut.clk, 1)
    dut.dval.value = 0
    await FallingEdge(dut.rdy)

    result = bin_to_float32(dut.result.value)
    dut._log.info("Result is %s", result)
    assert result == 1.5, "Adder failure"
