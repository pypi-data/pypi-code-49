#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse,sys,time
from pybuildit import *


method_subcmds = [
            "hold"
          , "force_hold"
          , "ready"
          , "force_ready"
          , "free"
          , "force_free"
          , "stop"
          , "clear_fault"
          , "reset_rotation"
          , "set_ref_current"
          , "get_ref_current"
          , "set_current_KP"
          , "get_current_KP"
          , "set_current_KI"
          , "get_current_KI"
          , "set_current_max_Iterm"
          , "get_current_max_Iterm"
          , "set_current_min_Iterm"
          , "get_current_min_Iterm"
          , "set_current_max_limit"
          , "get_current_max_limit"
          , "set_current_min_limit"
          , "get_current_min_limit"
          , "set_ref_velocity"
          , "get_ref_velocity"
          , "set_velocity_KP"
          , "get_velocity_KP"
          , "set_velocity_KI"
          , "get_velocity_KI"
          , "set_velocity_KD"
          , "get_velocity_KD"
          , "set_velocity_max_Iterm"
          , "get_velocity_max_Iterm"
          , "set_velocity_min_Iterm"
          , "get_velocity_min_Iterm"
          , "set_velocity_max_limit"
          , "get_velocity_max_limit"
          , "set_velocity_min_limit"
          , "get_velocity_min_limit"
          , "set_ref_position"
          , "get_ref_position"
          , "set_position_KP"
          , "get_position_KP"
          , "set_position_KI"
          , "get_position_KI"
          , "set_position_KD"
          , "get_position_KD"
          , "set_position_max_Iterm"
          , "get_position_max_Iterm"
          , "set_position_min_Iterm"
          , "get_position_min_Iterm"
          , "set_position_max_limit"
          , "get_position_max_limit"
          , "set_position_min_limit"
          , "get_position_min_limit"
          , "set_position_offset"
          , "get_position_offset"
          , "set_device_id"
          , "get_device_id"
          , "get_firmware_version"
          , "set_position_sys_offset"
          , "get_position_sys_offset"
          , "get_calibration_data"
          , "get_prot_stop_pin_timeout"
          , "get_stop_error_threshold"
          , "fault"
          , "print_log"
          , "get_power_on_time"
          , "find_device_id"
          , "save_servo_params"
          , "load_servo_params"
          , "save_configuration"
          ]

unsafe_subcmds = [
            "set_calibration_data"
          , "set_prot_stop_pin_timeout"
          , "set_stop_error_threshold"
          , "reset"
          , "clear_log"
          , "clear_power_on_time"
          , "debug"
          ]

ext_subcmds = [
            "query_servo_status"
          , "dump_query_servo_status"
          , "move"
          , "calib"
          ]

def create_buildit(args):
    return UnsafeBuildit(baud=args.baud, port=args.port, timeout_ms=args.timeout)


def cmd_query_servo_status(args):
    buildit = create_buildit(args)
    (pos, vel, cur, ref, temp, faults) = buildit.query_servo_status(args.deviceId).tuple()
    print("state:", buildit.last_mcp_status().str_state())
    print("pos:", pos)
    print("vel:", vel)
    print("pos[deg]:", to_deg(pos))
    print("vel[rpm]:", to_rpm(vel))
    print("cur:", cur)
    print("ref:", ref)
    print("temp:", temp)
    print("faults:", faults2str(faults))
    buildit.close()

def cmd_dump_query_servo_status(args):
    buildit = create_buildit(args)
    start = time.time()
    cnt = 0
    duration_sec = args.duration / 1000.0
    sleep_sec = args.sleep / 1000.0
    print("time[ms]", "pos[deg]", "vel[rpm]", "cur")
    while True:
        try:
            t = time.time()
            duration = t - start
            if duration_sec >= 0 and duration > duration_sec and duration_sec >= 0:
                break
            (pos, vel, cur, ref, temp, faults) = buildit.query_servo_status(args.deviceId).tuple()
            print((int((t-start) * 1000), to_deg(pos), to_rpm(vel), cur))
            if sleep_sec > 0 :
                time.sleep(sleep_sec)
            cnt += 1
        except TimeoutError:
            print("timeout")
            continue
    print (cnt / duration, "Hz")
    buildit.close()

def cmd_move(args):
    buildit = create_buildit(args)
    buildit.move_with_period(args.deviceId, args.goal, args.period, args.acc, args.dec, args.pos_thres, args.unit)

def cmd_calib(args):
    buildit = create_buildit(args)
    calibrate(buildit, args.deviceId, args.cur, args.span)

def common_parser(parser):
    parser.add_argument('-d', '--deviceId', type=int, default=1, help='deviceID(default: 1)')
    parser.add_argument('-p', '--port', type=str, default='/dev/ttyUSB0', help='device file (ex. /dev/ttyUSB0) or COM port number (ex. COM4). default value is /dev/ttyUSB0')
    parser.add_argument('-b', '--baud', type=int, default='115200', help='baudrate (default: 115200)')
    parser.add_argument('-t', '--timeout', type=float, default='3000', help='timeout[ms] (default: 3000)')
    parser.add_argument('-u', '--unit', type=str, default='raw', help='input/output unit (ex: raw,deg,rpm, default: raw)')
    return parser

def main():

    parser = argparse.ArgumentParser(
            prog='builditctl',
            description='utility program for Buildit/Buildit protocol communication'
            )

    subparsers = parser.add_subparsers()

    isUnsafeMode = int(os.getenv('UNSAFE_BUILDIT', 0)) == 1

    methods = method_subcmds + (unsafe_subcmds if isUnsafeMode else [])

    for subcmd in methods + ext_subcmds:
        subcmd_cli = subcmd.replace("_", '-')
        subparser = common_parser(subparsers.add_parser(subcmd_cli, help='see `{} -h`'.format(subcmd_cli)))
        subparser.set_defaults(subcmd=subcmd)

        if subcmd == 'stop':
            subparser.add_argument('-T', '--stoptimeout', type=int, default=500, help='stop-timeout [ms]')
            subparser.set_defaults(args2list=lambda args:[args.deviceId, args.stoptimeout])
        elif subcmd == 'set_ref_current':
            subparser.add_argument('ref', type=int, help='current reference value')
            subparser.set_defaults(args2list=lambda args:[args.deviceId, args.ref])
        elif subcmd == 'set_ref_velocity':
            subparser.add_argument('ref', type=int, help='velocity reference value')
            subparser.set_defaults(args2list=lambda args:[args.deviceId, args.ref, args.unit])
        elif subcmd == 'set_ref_position':
            subparser.add_argument('ref', type=int, help='position reference value')
            subparser.set_defaults(args2list=lambda args:[args.deviceId, args.ref, args.unit])
        elif subcmd.startswith('reset_rotation'):
            subparser.add_argument('value', type=int, help='value')
            subparser.set_defaults(args2list=lambda args:[args.deviceId, args.value])
        elif subcmd.startswith('set_'):
            subparser.add_argument('value', type=float, help='value')
            subparser.set_defaults(args2list=lambda args:[args.deviceId, args.value])
        elif subcmd == 'fault':
            subparser.add_argument('faults', type=int, help='fault values')
            subparser.set_defaults(args2list=lambda args:[args.deviceId, args.faults])
        elif subcmd == 'debug':
            subparser.add_argument('mode', type=int, help='mode(0:none, 1:position, 2:velocity)')
            subparser.set_defaults(args2list=lambda args:[args.deviceId, args.mode])
        elif subcmd == 'find_device_id':
            subparser.set_defaults(args2list=lambda args:[])
        elif subcmd == 'load_servo_params':
            subparser.add_argument('filepath', type=str, help='parameter file path')
            subparser.set_defaults(args2list=lambda args:[args.deviceId, args.filepath])
        elif subcmd == 'save_servo_params':
            subparser.add_argument('filepath', type=str, help='parameter file path')
            subparser.set_defaults(args2list=lambda args:[args.deviceId, args.filepath])
        elif subcmd == 'save_configuration':
            subparser.add_argument('filepath', type=str, help='parameter file path')
            subparser.set_defaults(args2list=lambda args:[args.deviceId, args.filepath])
        elif subcmd == 'dump_query_servo_status':
            subparser.add_argument('-D', '--duration', type=float, default=-1, help='duration [ms]')
            subparser.add_argument('-s', '--sleep', type=float, default=0, help='sleep [ms]')
        elif subcmd == 'move':
            subparser.add_argument('goal', type=float, help='goal position')
            subparser.add_argument('period', type=float, help='period [msec]')
            subparser.add_argument('--acc', type=float, default=0.2, help='acceleration period rate')
            subparser.add_argument('--dec', type=float, default=0.2, help='deceleration period rate')
            subparser.add_argument('--pos-thres', type=float, default=10, help='position error threshold')
        elif subcmd == 'calib':
            subparser.add_argument('--cur', type=int, default=2000, help='current reference value')
            subparser.add_argument('--span', type=int, default=1000, help='acceleration span [ms]')
        elif subcmd in methods:
            subparser.set_defaults(args2list=lambda args:[args.deviceId])

    args = parser.parse_args()

    if "subcmd" not in args.__dict__:
        parser.print_help()
        sys.exit(-1)

    if args.subcmd in methods:
        buildit = create_buildit(args)
        invoker = getattr(buildit, args.subcmd)
        methodarglist = args.args2list(args)
        result = invoker(*methodarglist)
        if result != () and result != None:
            print(result)
        buildit.close()
    elif args.subcmd == "query_servo_status":
       cmd_query_servo_status(args)
    elif args.subcmd == "dump_query_servo_status":
       cmd_dump_query_servo_status(args)
    elif args.subcmd == "move":
       cmd_move(args)
    elif args.subcmd == "calib":
       cmd_calib(args)


if __name__ == '__main__':
    main()
