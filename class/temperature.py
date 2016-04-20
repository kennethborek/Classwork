def GetTemperatures():

     Entry="yes"
     while (Entry=="yes" or Entry=="Yes" ):
         x = float(input("What is the temperature in Farenheit"))
         c = (x - 32) / 1.8
         print("The temperature in celsuis is",c)
         Entry=input("Continue?yes or no")
GetTemperatures()




