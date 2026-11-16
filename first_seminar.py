import numpy as np
ex2
class ColorTranslation:
    def rgb_to_yub(self, rgb):
        #array filled empty with the shape of rgb entry
        yub = np.empty(rgb.shape)
        #formula from t1 slides page 46, those are the bt601 standard values
        yub[0] = 0.257 * rgb[0] + 0.504 * rgb[1] + 0.08 * rgb[2] + 16
        yub[1] = -0.148 * rgb[0] - 0.291 * rgb[1] + 0.439 * rgb[2] + 128
        yub[2] = 0.439 * rgb[0] - 0.368 * rgb[1] - 0.071 * rgb[2] + 128
        return yub
    def yub_to_rgb(self, yub):
        rgb = np.empty(yub.shape)
        #formula from t1 slides page 46, those are the bt601 standard values
        rgb[0] = (yub[0] - 16) * 1.164 + 1.596 * (yub[2]-128)
        rgb[1] = (yub[0] - 16) * 1.164 - 0.813 * (yub[2]-128) - 0.391 * (yub[1]-128)
        rgb[2] = (yub[0] - 16) * 1.164 + 2.018 * (yub[1]-128)
        return rgb