from ophyd.controls import EpicsMotor, PVPositioner

# M1A

# args = ('XF:23IDA-OP:1{Mir:1-Ax:Z}Mtr_POS_SP',
#        {'readback': 'XF:23IDA-OP:1{Mir:1-Ax:Z}Mtr_MON',
#         'act': 'XF:23IDA-OP:1{Mir:1}MOVE_CMD.PROC',
#         'act_val': 1,
#         'stop': 'XF:23IDA-OP:1{Mir:1}STOP_CMD.PROC',
#         'stop_val': 1,
#         'done': 'XF:23IDA-OP:1{Mir:1}BUSY_STS',
#         'done_val': 0,
#         'name': 'm1a_z',
#        })
# m1a_z = PVPositioner(args[0], **args[1])


# Slits

slt_wb_tb = EpicsMotor('XF:05IDA-OP:1{Slt:1-Ax:T}Mtr', name='slt_wb_tb')
slt_wb_bb = EpicsMotor('XF:05IDA-OP:1{Slt:1-Ax:B}Mtr', name='slt_wb_bb')
slt_wb_ib = EpicsMotor('XF:05IDA-OP:1{Slt:1-Ax:I}Mtr', name='slt_wb_ib')
slt_wb_ob = EpicsMotor('XF:05IDA-OP:1{Slt:1-Ax:O}Mtr', name='slt_wb_ob')

slt_pb_ib = EpicsMotor('XF:05IDA-OP:1{Slt:2-Ax:I}Mtr', name='slt_pb_ib')
slt_pb_ob = EpicsMotor('XF:05IDA-OP:1{Slt:2-Ax:O}Mtr', name='slt_pb_ob')


# HFM Mirror

hfm_x = EpicsMotor('XF:05IDA-OP:1{Mir:1-Ax:X}Mtr', name='hfm_x')
hfm_y = EpicsMotor('XF:05IDA-OP:1{Mir:1-Ax:Y}Mtr', name='hfm_y')
hfm_pit = EpicsMotor('XF:05IDA-OP:1{Mir:1-Ax:P}Mtr', name='hfm_pit')
hfm_bdr = EpicsMotor('XF:05IDA-OP:1{Mir:1-Ax:Bend}Mtr', name='hfm_bdr')

# HDCM

dcm_bragg = EpicsMotor('XF:05IDA-OP:1{Mono:HDCM-Ax:P}Mtr', name='dcm_bragg')
dcm_c2_pitch = EpicsMotor('XF:05IDA-OP:1{Mono:HDCM-Ax:P2}Mtr', name='dcm_c2_pitch')
dcm_c1_roll = EpicsMotor('XF:05IDA-OP:1{Mono:HDCM-Ax:R1}Mtr', name='dcm_c1_roll')
dcm_gap = EpicsMotor('XF:05IDA-OP:1{Mono:HDCM-Ax:R1}Mtr', name='c_gap')
dcm_x = EpicsMotor('XF:05IDA-OP:1{Mono:HDCM-Ax:X}Mtr', name='dcm_x')
dcm_y = EpicsMotor('XF:05IDA-OP:1{Mono:HDCM-Ax:Y}Mtr', name='dcm_y')