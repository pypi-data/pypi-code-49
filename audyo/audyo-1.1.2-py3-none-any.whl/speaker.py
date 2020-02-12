import wave
import pyaudio


class Speaker(object):

    @staticmethod
    def play(file_path, chunk=1024):
        f = wave.open(file_path, "rb")
        # instantiate PyAudio
        p = pyaudio.PyAudio()
        # open stream
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        # read data
        data = f.readframes(chunk)

        # play stream
        while data:
            stream.write(data)
            data = f.readframes(chunk)

            # stop stream
        stream.stop_stream()
        stream.close()

        # close PyAudio
        p.terminate()


def main(play_file="audyo.wav"):
    Speaker.play(play_file)


if __name__ == "__main__":
    main()
