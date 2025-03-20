import cv2
import numpy as np
import mss
import time


class ScreenRecorder:
    def __init__(
        self, screen_size=None, fps=58.0, output_filename="gravacao.mp4", duration=15
    ):
        # Setup
        if screen_size is None:
            screen_size = {
                "top": 0,
                "left": 0,
                "width": 1366,
                "height": 768,
            }
        self.screen_size = screen_size
        self.fps = fps
        self.output_filename = output_filename
        self.duration = duration

        # Create recorder object
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.out = cv2.VideoWriter(
            self.output_filename,
            fourcc,
            self.fps,
            (self.screen_size["width"], self.screen_size["height"]),
        )

        # Create screenshot object
        self.sct = mss.mss()

    def start_recording(self):
        start_time = time.time()
        while (time.time() - start_time) < self.duration:
            # Capture the screen
            img = self.sct.grab(self.screen_size)
            frame = np.array(img)
            # Convert
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
            self.out.write(frame)
        self.out.release()
        cv2.destroyAllWindows()


# How to use:
if __name__ == "__main__":
    # Criar uma instância da classe ScreenRecorder com parâmetros personalizados
    recorder = ScreenRecorder(
        fps=30.0, output_filename="gravacao_customizada.mp4", duration=10
    )
    recorder.start_recording()
