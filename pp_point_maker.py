from xml.sax import SAXNotSupportedException
from pydub import AudioSegment
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


def main():
    sound = AudioSegment.from_mp3('nagareboshi_piano_ver.mp3')
    channel_count = sound.channels
    fps = sound.frame_rate
    duration = sound.duration_seconds

    print(f'channel_count:{channel_count} fps:{fps} duration:{duration}')

    data = np.array(sound.get_array_of_samples())
    x = data[::sound.channels]

    plt.plot(x[::10])
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()
