import imageio
import numpy as np
from PIL import Image
from moviepy.editor import *

class MP4VideoWriter:
    def __init__(self, filename, fps):
        self.filename = filename
        self.fps = fps
        self.frames = []

    def add_frame(self, pil_image):
        # Check if the image mode is supported
        if pil_image.mode not in ["RGB", "RGBA"]:
            raise ValueError("Unsupported image mode: {}".format(pil_image.mode))
        
        self.frames.append(pil_image)
        if len(self.frames) == 100:
            self.export_video()



    def export_video(self):
        self.append_images_to_mp4()
        self.frames = []
        # with imageio.get_writer(self.filename, mode='I', fps=self.fps) as writer:
        #     for frame in self.frames:
        #         np_image = np.array(frame)
        #         writer.append_data(np_image)

    def append_images_to_mp4(self):
        # Convert PIL images to numpy arrays
        np_frames = [np.array(image) for image in self.frames]

        # Create an ImageClip for each numpy array
        image_clips = [ImageClip(image, duration=1/self.fps) for image in np_frames                                                                                                                                                     ]
        # image_clips = [ImageClip(np_frame) for np_frame in np_frames]

        # Concatenate the ImageClips into a single VideoClip
        video_clip = concatenate_videoclips(image_clips, method="compose")
        
        # Load the existing MP4 file as a CompositeVideoClip
        existing_clip = CompositeVideoClip([VideoFileClip(self.filename).subclip(0)])

        # Append the VideoClip to the end of the existing clip
        existing_clip.set_duration(existing_clip.duration + video_clip.duration)
        
        final_clip = concatenate_videoclips([existing_clip, video_clip])

        # Write the final clip to a new MP4 file
        final_clip.write_videofile(self.filename)
