import sys
from time import sleep
from agw import Cursor
from agw import MsgBox
from .util import ctrl_exit
from .util import output_final_status


@ctrl_exit
@output_final_status("named_positions", "Named Positions", dict)
def position(*args, **kwargs):

    cursor = Cursor()
    last_position = (-1, -1)

    prompt_after_seconds = int(kwargs.get("prompt_for_name", 0))
    pause_time = float(kwargs.get("pause_time", 1))
    captured_named_positions = kwargs["named_positions"]


    prompt_count = 0

    while True:

        current_position = cursor.position

        if current_position == last_position:
            sys.stdout.write("*")
            sys.stdout.flush()
            prompt_count += 1

            if prompt_after_seconds > 0 and prompt_count == prompt_after_seconds:
                position_name = MsgBox.input(
                    f"Label current position ({current_position[0]}, {current_position[1]}):"
                )

                if position_name:
                    captured_named_positions[position_name] = (current_position[0], current_position[1])
                    print(f"\n{position_name}: {current_position[0]} {current_position[1]}")
                prompt_count = 0
                last_position = (-1, -1)

        else:
            last_position = current_position
            x, y = current_position
            sys.stdout.write("\n")
            sys.stdout.write(f"x: {x: >4}  y: {y: >4} ")
            sys.stdout.flush()

        sleep(pause_time)
