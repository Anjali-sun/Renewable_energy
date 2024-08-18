pip install opendatasets
#opendatasets is a Python library for downloading datasets 
#from online sources like Kaggle and Google Drive 
#using a simple Python command
#datasets already installed in this PC using the command 
#pip install opendatasets

#step 1
#import opendatasets library as od
import opendatasets as od

#import pandas as pd
import pandas as pd

#using download function of od, download following datasets from kaggle
#while downloading it will ask for kaggle username and passwd
#kaggle username - anjuviipin@gmail.com

#od.download("https://www.kaggle.com/datasets/jamesvandenberg/renewable-power-generation/")
od.download("https://www.kaggle.com/datasets/belayethossainds/renewable-energy-world-wide-19652022")
#datadir=./renewable-energy-world-wide-19652022 #<- test this.
file='renewable-energy-world-wide-19652022/renewable-share-energy.csv'
print (file)
newdata3=pd.read_csv(file1)
newdata3

#----------------------------------------
#DOWNLOAD JSON FROM GITHUB REPOSITORY 
#Uncomment the following section only. 
#import requests #Import requests module.
#url="https://raw.githubusercontent.com/Anjali-sun/data_sci/main/RoadWorks.json" #make sure that raw.githubusercontent.com is used. cannot be downloaded from github html.
#req=requests.get(url) #get the JSON from the above URL
#data=req.json() #convert to JSON 
#print (data)
#END of Downloading from GITHUB Code
#--------------------------------------
