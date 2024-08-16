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
#file1=("renewable-power-generation/top20CountriesPowerGeneration.csv")
#file2=("renewable-power-generation/renewablesTotalPowerGeneration.csv")
#newdata1=pd.read_csv(file1)
#newdata2=pd.read_csv(file2)
#print("printing TOP20 Countries Power Generation")
#print(newdata1)
#print(newdata2)
file='renewable-energy-world-wide-19652022/renewable-share-energy.csv'
print (file)
newdata3=pd.read_csv(file1)
newdata3
