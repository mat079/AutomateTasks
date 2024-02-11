import utils
import time

""" INIT VARIABLES"""
#CoinGecko variabes
url_CG = "https://www.coingecko.com/account/candy?locale=fr"
cookiesPath_CG = "cookiesCoinGecko.txt"
collectButton_CG = "collect-candy-button"

#initWebDriver
wd = utils.initWebDriver()


""" MAIN ACTIONS """
#Collect candy CoinGecko
utils.connectWithCookies(wd,url_CG,cookiesPath_CG)
utils.clickOnButton(wd,collectButton_CG)         

time.sleep(20)

#Disconnect 
wd.close()
wd.quit()



