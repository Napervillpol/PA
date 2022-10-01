
import pandas as pd
def safediv(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0

class race:
    mail=[];
    eday=[];
    prov=[];
    def __init__(self, mail,eday,prov):
        self.mail=mail;
        self.eday=eday;
        self.prov=prov;

df = pd.read_csv('PA.csv');
df2= pd.read_csv('PA_2020.csv');

# 2020 President
Biden= df2.loc[(df2['Office Name']  =='President of the United States' ) & (df2['Party Name']  =='Democratic' )];
Trump= df2.loc[(df2['Office Name']  =='President of the United States' ) & (df2['Party Name']  =='Republican' )];

#Mail 
Biden_mail = Biden[['County Name','Mail Votes']];
Biden_mail.columns=['County','Biden'];

Trump_mail = Trump[['County Name','Mail Votes']];
Trump_mail.columns=['County','Trump'];
mail = Biden_mail.merge(Trump_mail, on='County')

#Election day
Biden_eday = Biden[['County Name','Election Day Votes']];
Biden_eday.columns=['County','Biden'];

Trump_eday = Trump[['County Name','Election Day Votes']];
Trump_eday.columns=['County','Trump'];
eday = Biden_eday.merge(Trump_eday, on='County')

#Provisonal
Biden_prov= Biden[['County Name','Provisional Votes']];
Biden_prov.columns=['County','Biden'];

Trump_prov = Trump[['County Name','Provisional Votes']];
Trump_prov.columns=['County','Trump'];
prov = Biden_prov.merge(Trump_prov, on='County')

President = race(mail,eday,prov);


Fetterman = df.loc[(df['Office Name']  =='United States Senator' ) & (df['Party Name']  =='Democratic' )];


print(President.eday)