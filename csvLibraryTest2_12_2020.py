import csv
import board
import busio
import adafruit_character_lcd.character_lcd_rgb_i2c as character_lcd
lcd_columns = 16
lcd_rows = 2
i2c = busio.I2C(board.SCL, board.SDA)
lcd = character_lcd.Character_LCD_RGB_I2C(i2c, lcd_columns, lcd_rows)

lcd.clear()

lcd.message = "initializing\nPlease Wait."
time.sleep(2)
lcd.clear()


lcd.message = "initializing\nPlease Wait.."
time.sleep(2)
lcd.clear()

lcd.message = "initializing\nPlease Wait..."
time.sleep(2)
lcd.clear()

lcd.message = "initializing\nPlease Wait."
time.sleep(2)
lcd.clear()

lcd.message = "initializing\nPlease Wait.."
time.sleep(2)
lcd.clear()

lcd.message = "initializing\nPlease Wait..."
time.sleep(2)
lcd.clear()

lcd.message = "initializing\nPlease Wait."
time.sleep(2)
lcd.clear()


lcd.message = "initializing\nPlease Wait."
time.sleep(2)
lcd.clear()

lcd.message = "initializing\nPlease Wait.."
time.sleep(2)
lcd.clear()

lcd.message = "initializing\nPlease Wait..."
time.sleep(2)
lcd.clear()


lcd.message = "initializing\nPlease Wait."
time.sleep(2)
lcd.clear()



with open("cityinv.csv", 'r') as scoreFile:
    csvReader = csv.reader(scoreFile)
    Asset = input("Enter Asset:")
    for row in csvReader:
        if row[0] == Asset:
                x=row[14]
                if(x=="Deployed"):
                        print([Asset])
                        print("Item is Deployed")

                if(x=="Received"):
                        print([Asset])
                        print("Item is Received")

                if(x=="Mayor Sign Off"):
                        print([Asset])
                        print("Item is Mayor Sign Off")

                if(x=="Surplus"):
                        print([Asset])
                        print("Item is Surplus")

                if(x=="Warehoused"):
                        print([Asset])
                        print("Item is Warehoused")
