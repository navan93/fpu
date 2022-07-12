# FPU
IEEE 754 floating-point unit which supports standard RISC-V operations, written in Verilog.

## Operations

| Instruction  | Operation | Implementation Status | Notes |
| ------  | --------- | ------ | ------- |
| FMADD.S | Fused multiply-add, `(rs1 * rs2) + rs3` | TBD | |
| FMSUB.S | Fused multiply-subtract, `(rs1 * rs2) - rs3` | TBD | |
| FNMSUB.S | Negated fused multiply-subtract, `-(rs1 * rs2) + rs3` | TBD | |
| FNMADD.S | Negated fused multiply-add, `-(rs1 * rs2) - rs3` | TBD | |
| FADD.S | Addition, `rs1 + rs2` | :heavy_check_mark: | |
| FSUB.S | Subtraction, `rs1 - rs2` | :heavy_check_mark: | |
| FMUL.S | Multiplication, `rs1 * rs2` | :heavy_check_mark: | |
| FDIV.S | Division, `rs1 / rs2` | :heavy_check_mark: | |
| FSQRT.S | Square root of `rs1` | TBD | |
| FSGNJ.S | Sign injection, `rs1` with `sign(rs2)` | TBD | |
| FSGNJN.S | Sign injection, `rs1` with `~sign(rs2)` | TBD | |
| FSGNJX.S | Sign injection, `rs1` with `sign(rs1) ^ sign(rs2)` | TBD | |
| FMIN.S | Minimum, `minimumNumber(rs1, rs2)` | TBD | |
| FMAX.S | Maximum, `maximumNumber(rs1, rs2)` | TBD | |
| FCVT.W.S | Convert `rs1` to signed interger | :heavy_check_mark: | src is FP register, dest is INT register |
| FCVT.WU.S | Convert `rs1` to unsigned interger | :heavy_check_mark: | src is FP register, dest is INT register |
| FMV.X.W | Move value in floating-point register `rs1` to integer register `rd` | TBD | src is FP register, dest is INT register |
| FEQ.S | Comparison, `rs1 == rs2`. Write 1 to the integer register `rd` if the condition holds, and 0 otherwise. | TBD | src is FP register, dest is INT register |
| FLT.S | Comparison, `rs1 < rs2`. Write 1 to the integer register `rd` if the condition holds, and 0 otherwise. | TBD | src is FP register, dest is INT register |
| FLE.S | Comparison, `rs1 <= rs2`. Write 1 to the integer register `rd` if the condition holds, and 0 otherwise. | TBD | src is FP register, dest is INT register |
| FCLASS.S | Classification, examine the value in floating-point register `rs1` and write to integer register `rd` a 10-bit mask that indicates the class of the floating-point number | TBD | src is FP register, dest is INT register |
| FCVT.S.W | Convert signed interger `rs1` to FP in `rd` | :heavy_check_mark: | src is INT register, dest is FP register |
| FCVT.S.WU | Convert unsigned interger `rs1` to FP in `rd` | :heavy_check_mark: | src is INT register, dest is FP register |
| FMV.W.X | Move value in integer register `rs1` to floating-point register `rd` | TBD | src is INT register, dest is FP register |

