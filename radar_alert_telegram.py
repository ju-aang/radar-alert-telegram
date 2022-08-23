#Import packages
import numpy as np
import cv2
import imutils
import telegram
import schedule
import time

#Declare City
kota = 'TANG' ##take the first 4 letters and capitalize (Ex: Tangerang to TANG)

#Function
def monitoring_radar():
    ##load image
    url = 'https://inderaja.bmkg.go.id/Radar/'+ kota + '_SingleLayerCRefQC.png'
    image = imutils.url_to_image(url)
    image = image[100:1130, 100:1145] #crop image

    ##define color's treshold
    kuning = np.array([0, 254, 255]) #yellow tangerang
    mask = cv2.inRange(image, kuning, kuning)

    ##save image
    cv2.imwrite('timika.png', image)
    PHOTO_PATH = 'timika.png'

    #define telegram group
    TELEGRAM_BOT_TOKEN = '5391971893:AAEzh7L2kPE5oIFhSYYEsPJRbRXC7lbDp98'
    TELEGRAM_CHAT_ID = '-574994361'
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

    #Color detection
    count = np.sum(np.nonzero(mask))
    if count == 0:
        print("Tidak ada potensi hujan")
    else:
        #Send to telegram group
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="!!! Ada Potensi Hujan di Timika dan sekitarnya !!!")
        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(PHOTO_PATH, 'rb'))

#Schedule every 10 minutes
schedule.every(10).minutes.do(monitoring_radar)
while True:
	schedule.run_pending()
	time.sleep(1)
