
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
sb.set()
pd.options.mode.chained_assignment = None

def write_to_excel(race,race_name):
    writer = pd.ExcelWriter('PA_'+race_name+ '.xlsx', engine='xlsxwriter')

    race.mail.to_excel(writer,sheet_name="Mail",index=False)
    race.eday.to_excel(writer,sheet_name="Election Day",index=False)
    race.prov.to_excel(writer,sheet_name="Provisonal",index=False)
    race.total.to_excel(writer,sheet_name="Total",index=False)

    writer.save()

def safediv(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0

def calculations(df,Dem_name,Rep_name):
   
    df[Dem_name]=df[Dem_name].astype(str)
    df[Rep_name]=df[Rep_name].astype(str)
    
    df[Dem_name]=df[Dem_name].str.replace(',','')
    df[Rep_name]=df[Rep_name].str.replace(',','')

    df[Dem_name]=df[Dem_name].astype(int)
    df[Rep_name]=df[Rep_name].astype(int)
    
    df.insert(3, "Total", df[Dem_name]+df[Rep_name])
    df.insert(4, "Net Votes", df[Dem_name]-df[Rep_name])
    df.insert(5, Dem_name+" Pct", df[Dem_name]/(df[Dem_name]+df[Rep_name]))
    df.insert(6, Rep_name+" Pct", df[Rep_name]/(df[Dem_name]+df[Rep_name]))
    df.insert(7, "Margin",(df[Dem_name]/(df[Dem_name]+df[Rep_name])) -(df[Rep_name]/(df[Dem_name]+df[Rep_name])))


def calculate_shift(df_2022,df_2020):
     
     df_2022.mail.insert(8, "Pct Shift",df_2022.mail["Margin"]-df_2020.mail["Margin"])
     df_2022.mail.insert(9, "Turnout",df_2022.mail["Total"]/df_2020.mail["Total"])

     df_2022.eday.insert(8, "Pct Shift",df_2022.eday["Margin"]-df_2020.eday["Margin"])
     df_2022.eday.insert(9, "Turnout",df_2022.eday["Total"]/df_2020.eday["Total"])

     df_2022.prov.insert(8, "Pct Shift",df_2022.prov["Margin"]-df_2020.prov["Margin"])
     df_2022.prov.insert(9, "Turnout",df_2022.prov["Total"]/df_2020.prov["Total"])

     df_2022.total.insert(8, "Pct Shift",df_2022.total["Margin"]-df_2020.total["Margin"])
     df_2022.total.insert(9, "Turnout",df_2022.total["Total"]/df_2020.total["Total"])

def MailProjection(df2,df3):
    #print(df2.mail)
    #print(df3)
    df2.mail= df2.mail.merge(df3,on="County")
    df2.mail.insert(11,"Outstanding Ballots",df2.mail["Accepted Ballots"]-df2.mail["Total"])
    df2.mail.insert(12,"Dem Oustanding",round(df2.mail.iloc[:, 5]*df2.mail["Outstanding Ballots"],0))
    df2.mail.insert(13,"Rep Oustanding",round(df2.mail.iloc[:, 6]*df2.mail["Outstanding Ballots"],0))
    df2.mail.insert(14,"Net Oustanding",df2.mail["Dem Oustanding"]-df2.mail["Rep Oustanding"])

  

def addTotalVotes(df,df1,df2):
    
    Senate_race= df.loc[(df['Office Name']  =='United States Senator' )]
    Governor_race = df.loc[(df['Office Name']  =='Governor' )]
    
    Senate_race['Votes'] =  Senate_race['Votes'].astype(str)
    Senate_race['Votes'] =  Senate_race['Votes'].str.replace(',','')
    Senate_race['Votes'] =  Senate_race['Votes'].astype(int)

    Senate_race['Election Day Votes'] =  Senate_race['Election Day Votes'].astype(str)
    Senate_race['Election Day Votes'] =  Senate_race['Election Day Votes'].str.replace(',','')
    Senate_race['Election Day Votes'] =  Senate_race['Election Day Votes'].astype(int)

    Senate_race['Mail Votes'] =  Senate_race['Mail Votes'].astype(str)
    Senate_race['Mail Votes'] =  Senate_race['Mail Votes'].str.replace(',','')
    Senate_race['Mail Votes'] =  Senate_race['Mail Votes'].astype(int)

    Senate_race['Provisional Votes'] =  Senate_race['Provisional Votes'].astype(str)
    Senate_race['Provisional Votes'] =  Senate_race['Provisional Votes'].str.replace(',','')
    Senate_race['Provisional Votes'] =  Senate_race['Provisional Votes'].astype(int)

   
    Governor_race['Votes'] =  Governor_race['Votes'].astype(str)
    Governor_race['Votes'] =  Governor_race['Votes'].str.replace(',','')
    Governor_race['Votes'] =  Governor_race['Votes'].astype(int)

    Governor_race['Election Day Votes'] =  Governor_race['Election Day Votes'].astype(str)
    Governor_race['Election Day Votes'] =  Governor_race['Election Day Votes'].str.replace(',','')
    Governor_race['Election Day Votes'] =  Governor_race['Election Day Votes'].astype(int)

    Governor_race['Mail Votes'] =  Governor_race['Mail Votes'].astype(str)
    Governor_race['Mail Votes'] = Governor_race['Mail Votes'].str.replace(',','')
    Governor_race['Mail Votes'] =  Governor_race['Mail Votes'].astype(int)

    Governor_race['Provisional Votes'] = Governor_race['Provisional Votes'].astype(str)
    Governor_race['Provisional Votes'] = Governor_race['Provisional Votes'].str.replace(',','')
    Governor_race['Provisional Votes'] =  Governor_race['Provisional Votes'].astype(int)


    Senate_race = Senate_race.groupby(Senate_race['County Name'])[['Votes','Election Day Votes','Mail Votes','Provisional Votes']].sum().reset_index()
    Governor_race =  Governor_race.groupby(Governor_race['County Name'])[['Votes','Election Day Votes','Mail Votes','Provisional Votes']].sum().reset_index()

  
    
    df1.total['Total'] =Senate_race['Votes']
    df1.mail['Total'] =Senate_race['Mail Votes']
    df1.eday['Total'] =Senate_race['Election Day Votes']
    df1.prov['Total'] =Senate_race['Provisional Votes']

    df2.total['Total'] =Governor_race['Votes']
    df2.mail['Total'] =Governor_race['Mail Votes']
    df2.eday['Total'] =Governor_race['Election Day Votes']
    df2.prov['Total'] =Governor_race['Provisional Votes']
 
  


class race:
    mail=[]
    eday=[]
    prov=[]
    total=[]
    def __init__(self, mail,eday,prov,total):
        self.mail=mail
        self.eday=eday
        self.prov=prov
        self.total=total

def assign_race(Dem,Rep,Dem_name,Rep_name):
       
    #Mail 
    Dem_mail = Dem[['County Name','Mail Votes']]
    Dem_mail.columns=['County',Dem_name]

    Rep_mail = Rep[['County Name','Mail Votes']]
    Rep_mail.columns=['County',Rep_name]
    mail = Dem_mail.merge(Rep_mail, on='County')
    calculations(mail,Dem_name,Rep_name)
   
    #Election day
    Dem_eday = Dem[['County Name','Election Day Votes']]
    Dem_eday.columns=['County',Dem_name]

    Rep_eday = Rep[['County Name','Election Day Votes']]
    Rep_eday.columns=['County',Rep_name]
    eday = Dem_eday.merge(Rep_eday, on='County')
    calculations(eday,Dem_name,Rep_name)

    #Provisonal
    Dem_prov= Dem[['County Name','Provisional Votes']]
    Dem_prov.columns=['County',Dem_name]

    Rep_prov = Rep[['County Name','Provisional Votes']]
    Rep_prov.columns=['County',Rep_name]
    prov = Dem_prov.merge(Rep_prov, on='County')
    calculations(prov,Dem_name,Rep_name)

     #Total
    Dem_total= Dem[['County Name','Votes']]
    Dem_total.columns=['County',Dem_name]

    Rep_total = Rep[['County Name','Votes']]
    Rep_total.columns=['County',Rep_name]
    total = Dem_total.merge(Rep_total, on='County')
    calculations(total,Dem_name,Rep_name)

    Race = race(mail,eday,prov,total)
    return Race;


#df = pd.read_csv('PA.csv')
df2= pd.read_csv('PA_2020.csv')
df3 = pd.read_csv('PA_ABSENTEES.csv')
df = pd.read_csv('2022General.csv')


# 2020 President
Biden= df2.loc[(df2['Office Name']  =='President of the United States' ) & (df2['Party Name']  =='Democratic' )]
Trump= df2.loc[(df2['Office Name']  =='President of the United States' ) & (df2['Party Name']  =='Republican' )]
President = assign_race(Biden,Trump,"Biden","Trump")

# 2022 Senate
Fetterman= df.loc[(df['Office Name']  =='United States Senator' ) & (df['Party Name']  =='Democratic' )]
Oz= df.loc[(df['Office Name']  =='United States Senator' ) & (df['Party Name']  =='Republican' )]
Senate = assign_race(Fetterman,Oz,"Fetterman","Oz")
calculate_shift(Senate,President)


# 2022 Gov
Shapiro= df.loc[(df['Office Name']  =='Governor' ) & (df['Party Name']  =='Democratic' )]
Mastriano= df.loc[(df['Office Name']  =='Governor' ) & (df['Party Name']  =='Republican' )]
Governor = assign_race(Shapiro,Mastriano,"Shapiro","Mastriano")
calculate_shift(Governor,President)

addTotalVotes(df,Senate,Governor)
MailProjection(Senate,df3)
MailProjection(Governor,df3)


write_to_excel(President,"President")
write_to_excel(Senate,"Senate")
write_to_excel(Governor,"Governor")

plt.title('Senate (Mail)')
plt.scatter(Senate.mail['Fetterman Pct'],President.mail['Biden Pct'])

x = Senate.mail['Fetterman Pct'].dropna().reset_index()
y = President.mail['Biden Pct'].reset_index()

Sen_graph =x.merge(y,on="index")
Sen_graph=Sen_graph.drop(columns=['index'])

sb.regplot(x="Fetterman Pct",y="Biden Pct",fit_reg=True,data=Sen_graph)
plt.show()