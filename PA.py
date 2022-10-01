
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

def assign_race(Dem,Rep,Dem_name,Rep_name):
       
    #Mail 
    Dem_mail = Dem[['County Name','Mail Votes']];
    Dem_mail.columns=['County',Dem_name];

    Rep_mail = Rep[['County Name','Mail Votes']];
    Rep_mail.columns=['County',Rep_name];
    mail = Dem_mail.merge(Rep_mail, on='County')

    #Election day
    Dem_eday = Dem[['County Name','Election Day Votes']];
    Dem_eday.columns=['County',Dem_name];

    Rep_eday = Rep[['County Name','Election Day Votes']];
    Rep_eday.columns=['County',Rep_name];
    eday = Dem_eday.merge(Rep_eday, on='County')

    #Provisonal
    Dem_prov= Dem[['County Name','Provisional Votes']];
    Dem_prov.columns=['County',Dem_name];

    Rep_prov = Trump[['County Name','Provisional Votes']];
    Rep_prov.columns=['County',Rep_name];
    prov = Dem_prov.merge(Rep_prov, on='County')

    Race = race(mail,eday,prov);
    return Race;


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

# 2022 Senate
Fetterman= df.loc[(df['Office Name']  =='United States Senator' ) & (df['Party Name']  =='Democratic' )];
Oz= df.loc[(df['Office Name']  =='United States Senator' ) & (df['Party Name']  =='Republican' )];

President = assign_race(Biden,Trump,"Biden","Trump");
Senate = assign_race(Fetterman,Oz,"Fetterman","Oz");

print(President.mail)