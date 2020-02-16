from mido import Message, MidiFile, MidiTrack


class Track:
    def __init__(self, file_name, config, program):
        self.file_name = file_name
        self.output = MidiFile()
        self.track = MidiTrack()
        self.output.tracks.append(self.track)

        self.input_to_note = dict(zip(config['validInputs'], config['midiNotes']))
        self.fps = config['fps']

        self.track.append(Message('program_change', program=program, time=0))

        self.activated_notes = dict([(i, False) for i in config['validInputs']])
        self.beats_passed = 0

    def save(self):
        self.output.save(self.file_name)

    def handle(self, line):
        inputs = [i for i in line.split('|')[1].split(':') if i != '']

        self.disable_notes_not_in_input(inputs)

        for input_str in inputs:
            self.enable_note(input_str)

        self.beats_passed += 1

    def disable_notes_not_in_input(self, inputs):
        for input_name, activated in self.activated_notes.items():
            if activated and input_name not in inputs:
                self.activated_notes[input_name] = False
                self.track.append(
                    Message(
                        'note_off',
                        note=self.input_to_note[input_name],
                        time=self.delta,
                    ),
                )
                self.beats_passed = 0

    def enable_note(self, input_str):
        if self.activated_notes[input_str]:
            return

        self.activated_notes[input_str] = True
        self.track.append(
            Message(
                'note_on',
                note=self.input_to_note[input_str],
                velocity=64,
                time=self.delta,
            ),
        )
        self.beats_passed = 0

    @property
    def delta(self):
        return (self.beats_passed * self.output.ticks_per_beat) // (self.fps // 2)
