module tb_top;

reg          clk;
reg          rst_n;
reg [3:0]    cmd;
reg [31:0]   din1;
reg [31:0]   din2;
reg          dval;
wire [31:0] result;
reg [31:0]  c_result;
wire        rdy;
reg         test_fail;
integer     i;

wire USER_VDD1V8 = 1'b1;
wire VSS = 1'b0;


fpu_sp_top u_fpu_sp_top (
      `ifdef USE_POWER_PINS
          .vccd1 (USER_VDD1V8),// User area 1 1.8V supply
          .vssd1 (VSS),// User area 1 digital ground
      `endif

        .clk         (clk     ),
        .rst_n       (rst_n   ),
        .cmd         (cmd     ),
        .din1        (din1    ),
        .din2        (din2    ),
        .dval        (dval    ),
        .result      (result  ),
        .rdy         (rdy     )
      );

//initial begin
//   $dumpfile("simx.vcd");
//   $dumpvars(0, tb_top);
//end

endmodule
