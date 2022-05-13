import gspread

gc=gspread.service_account(filename="creds.json")
sh=gc.open("scrapetosheet").sheet1

#sh.update("A1","test")