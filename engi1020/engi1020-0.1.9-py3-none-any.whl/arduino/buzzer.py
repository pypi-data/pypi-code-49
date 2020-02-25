buzzer_instance = None

def get_buzzer(pin):
    """Get static reference to buzzer.

    Parameters:
      pin (int):       Digital connection port (range: [2, 8])
    """

    global buzzer_instance

    if buzzer_instance is None:
        from . import arduino, tone

        buzzer_instance = tone.Tone(pin, arduino().connection)

    return buzzer_instance

def note(pin, freq, duration):
    """Play note of given frequency

    Parameters:
      pin (int):       Digital connection port (range: [2, 8])
      freq (int):      Frequency of note in Hz
      duration (int):  Note length in seconds
    """

    get_buzzer(pin).play(freq, duration)

def stop(pin):
    """Stop note

    Parameters:
      pin (int):       Digital connection port (range: [2, 8])
    """

    get_buzzer(pin).stop()
