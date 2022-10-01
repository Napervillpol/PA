
import pandas as pd
def safediv(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0

def calculations(df,Dem_name,Rep_name):
   
    df[Dem_name]=df[Dem_name].str.replace(',','');  
    df[Rep_name]=df[Rep_name].str.replace(',','');
    
    df.insert(3, "Total", df[Dem_name].astype(int)+df[Rep_name].astype(int));

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
    mail = Dem_mail.merge(Rep_mail, on='County');
    calculations(mail,Dem_name,Rep_name);
   
    #Election day
    Dem_eday = Dem[['County Name','Election Day Votes']];
    Dem_eday.columns=['County',Dem_name];

    Rep_eday = Rep[['County Name','Election Day Votes']];
    Rep_eday.columns=['County',Rep_name];
    eday = Dem_eday.merge(Rep_eday, on='County')
    calculations(eday,Dem_name,Rep_name);

    #Provisonal
    Dem_prov= Dem[['County Name','Provisional Votes']];
    Dem_prov.columns=['County',Dem_name];

    Rep_prov = Trump[['County Name','Provisional Votes']];
    Rep_prov.columns=['County',Rep_name];
    prov = Dem_prov.merge(Rep_prov, on='County')
    calculations(prov,Dem_name,Rep_name);

    Race = race(mail,eday,prov);
    return Race;


df = pd.read_csv('PA.csv');
df2= pd.read_csv('PA_2020.csv');

# 2020 President
Biden= df2.loc[(df2['Office Name']  =='President of the United States' ) & (df2['Party Name']  =='Democratic' )];
Trump= df2.loc[(df2['Office Name']  =='President of the United States' ) & (df2['Party Name']  =='Republican' )];
President = assign_race(Biden,Trump,"Biden","Trump");

# 2022 Senate
Fetterman= df.loc[(df['Office Name']  =='United States Senator' ) & (df['Party Name']  =='Democratic' )];
Oz= df.loc[(df['Office Name']  =='United States Senator' ) & (df['Party Name']  =='Republican' )];
Senate = assign_race(Fetterman,Oz,"Fetterman","Oz");

# 2022 Gov
Shapiro= df.loc[(df['Office Name']  =='Governor' ) & (df['Party Name']  =='Democratic' )];
Mastriano= df.loc[(df['Office Name']  =='Governor' ) & (df['Party Name']  =='Republican' )];
Senate = assign_race(Shapiro,Mastriano,"Shapiro","Mastriano");

print(President.mail)
writer = pd.ExcelWriter('PA_Results.xlsx', engine='xlsxwriter');

President.mail.to_excel(writer,sheet_name="Mail",index=False);
President.eday.to_excel(writer,sheet_name="Election Day",index=False);
President.prov.to_excel(writer,sheet_name="Provisonal",index=False);

writer.save();