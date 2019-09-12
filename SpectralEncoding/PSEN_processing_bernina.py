from psen_processing import PsenProcessingClient
from bsread import source
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from datetime import datetime
# For Bernina PSEN

Camera_image = 'SARES20-CAMS142-M5:FPICTURE'
ROI_background = 'SARES20-CAMS142-M5:FPICTURE.roi_background_x_profile'
ROI_signal = 'SARES20-CAMS142-M5:FPICTURE.roi_signal_x_profile'

Channels = [Camera_image, ROI_background, ROI_signal]
with source(channels=Channels) as stream:
    message = stream.receive()


client =  PsenProcessingClient(address="http://sf-daqsync-02:12002/")
status_message = client.get_status()
roi_signal_message = client.get_roi_signal()
roi_background_message = client.get_roi_background()

print("Status of Bernina PSEN_proc "+status_message+"\nROI signal "+ str(roi_signal_message)+ "\nROI background "+str(roi_background_message))

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
