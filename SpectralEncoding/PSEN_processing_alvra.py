from bsread import source
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from datetime import datetime
# For PSEN Alvra

Camera_image = 'SARES11-SPEC125-M2:FPICTURE'
ROI_background = 'SARES11-SPEC125-M2.roi_background_x_profile'
ROI_signal = 'SARES11-SPEC125-M2.roi_signal_x_profile'

Channels = [Camera_image, ROI_background, ROI_signal]
with source(channels=Channels) as stream:
    message = stream.receive()


plt.figure()
plt.subplot(311)
plt.imshow(message.data.data[Camera_image].value)
plt.title(Camera_image+', pulse ID '+str(message.data.pulse_id)+'\n '+str(datetime.fromtimestamp(message.data.global_timestamp)))
#Axis = plt.gca()
#Axis.add_patch(Rectangle((roi_signal_message[0],roi_signal_message[3]),roi_signal_message[2],roi_signal_message[3]))
plt.subplot(312)
plt.plot(message.data.data[ROI_background].value)
plt.title('ROI background')

plt.subplot(313)
plt.plot(message.data.data[ROI_signal].value)
plt.title('ROI signal')

plt.show()
