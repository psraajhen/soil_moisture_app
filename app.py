# sudo apt-get update
# sudo apt-get install build-essential python-dev python-smbus git
# cd ~
# git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
# cd Adafruit_Python_ADS1x15
# sudo python setup.py install

# sudo apt-get update
# sudo apt-get install build-essential python-dev python-smbus python-pip
# sudo pip install adafruit-ads1x15

import time
import board
import busio
from flask import Flask, jsonify, render_template
from adafruit_ads1x15.analog_in import AnalogIn
import adafruit_ads1x15.ads1115 as ADS

app = Flask(__name__)

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channels 0, 1, and 2
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    soil_moisture_1 = chan0.value
    soil_moisture_2 = chan1.value
    soil_moisture_3 = chan2.value
    return jsonify({
        'soil_moisture_1': soil_moisture_1,
        'soil_moisture_2': soil_moisture_2,
        'soil_moisture_3': soil_moisture_3
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
