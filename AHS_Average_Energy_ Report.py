import pandas as pd
from datetime import datetime

#imports data created in assignment 1 and rounds the values
ahs_average_energy = pd.read_csv(r"C:\Users\shrey\OneDrive\Documents\5 Programming\Energize\Learning Pandas\averageEnergy.csv", skiprows=2, index_col=False)
average_energy= ahs_average_energy.round(0)

#seperates data and clumps data based on day of the week
report1 = average_energy[average_energy[' '] == 0]
report2 = average_energy[average_energy[' '] == 1]
report3 = average_energy[average_energy[' '] == 2]
report4 = average_energy[average_energy[' '] == 3]
report5 = average_energy[average_energy[' '] == 4]
report6 = average_energy[average_energy[' '] == 5]
report7 = average_energy[average_energy[' '] == 6]

report8 = pd.DataFrame({' ': [' '],
                        'Days': [' '],
                        'HS Main (kWh)': [' '],
                        'LV Plug Loads (DHB)':  [' '],
                        'HS DL Lighting (kWh)':  [' '],
                        'HS DG Gym (kWh)':  [' '],
                        'HS Kitchen Emergency (kWh)':  [' '],
                        'HS M1 Chillers (kWh)':  [' '],
                        'HS CC Collins Center (kWh)':  [' ']
                                   })
data = [report1,report8,report2,report8,report3,report8,report4,report8,report5,report8,report6,report8,report7,report8]
ahs_energy_data= pd.concat(data) # concats the all the data and basiclly reorganizes the data made in the last program, making it more readable and more formated
ahs_energy_Data = ahs_energy_data.drop([' '], axis=1)
ahs_energy_Data.insert(loc=0, column='Electricity used by AHS between 23:00 hrs and 4:00 hrs Total yearly saving over 2016: $4892.96 kWh Saved since 2016: 30581.0      ', value=" ")


#reads the data created in the previous program and removes any columns with strings
ahs_average_energy1 = pd.read_csv(r"C:\Users\shrey\OneDrive\Documents\5 Programming\Energize\Learning Pandas\averageEnergy.csv", skiprows=2, usecols=[' ',
                                                                                                                                                      'HS Main (kWh)',
                                                                                                                                                      'LV Plug Loads (DHB)',
                                                                                                                                                      'HS DL Lighting (kWh)',
                                                                                                                                                      'HS DG Gym (kWh)',
                                                                                                                                                      'HS Kitchen Emergency (kWh)',
                                                                                                                                                      'HS M1 Chillers (kWh)',
                                                                                                                                                      'HS CC Collins Center (kWh)'])

def average_reduction(day_of_week,ahs_energy,x,y):
    ahs_energy_day = ahs_energy[ahs_energy[' '] == day_of_week]
    pct_reduction = ahs_energy_day.pct_change(periods=2)
    pct1 = pct_reduction.drop([x, y])
    pct2 = pct1.mul(-100)
    pct3 = pct2.round(0)
    pct4 = pct3.drop([' '], axis=1)

    diff_reduction = ahs_energy_day.diff(periods=2)
    diff1 = diff_reduction.mul(-0.16)
    diff2 = diff1.drop([x, y])
    diff3 = diff2.drop([' '], axis=1)
    diff4 = diff3.round(2)
    return pct4, diff4 # a function that takes in data and sorts through them and return the percent change and cost difference over 2016

monday1, monday2 = average_reduction(0,ahs_average_energy1,0,7)  #stores the percent change and cost difference data for each day
tuesday1, tuesday2 = average_reduction(1,ahs_average_energy1,1,8)
wednesday1, wednesday2 = average_reduction(2,ahs_average_energy1,2,9)
thursday1, thursday2 = average_reduction(3,ahs_average_energy1,3,10)
friday1, friday2 = average_reduction(4,ahs_average_energy1,4,11)
saturday1, saturday2 = average_reduction(5,ahs_average_energy1,5,12)
sunday1, sunday2 = average_reduction(6,ahs_average_energy1,6,13)

data1 = [monday1, tuesday1, wednesday1, thursday1, friday1, saturday1, sunday1]
data2 = [monday2, tuesday2, wednesday2, thursday2, friday2, saturday2, sunday2]

ahs_reduction_pct= pd.concat(data1) # concats the percent change and cost difference data
ahs_reduction_diff= pd.concat(data2)

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
ahs_reduction_pct.insert(loc=0, column='Days', value=days) # adds the day column back to the data
ahs_reduction_pct.insert(loc=0, column=' ', value=" ")
ahs_reduction_diff.insert(loc=0, column='Days', value=days)
ahs_reduction_diff.insert(loc=0, column=' ', value=" ")


ahs_reduction_pct['HS Main (kWh)'] = ahs_reduction_pct['HS Main (kWh)'].astype(str) + '%'
ahs_reduction_pct['LV Plug Loads (DHB)'] = ahs_reduction_pct['LV Plug Loads (DHB)'].astype(str) + '%'
ahs_reduction_pct['HS DL Lighting (kWh)'] = ahs_reduction_pct['HS DL Lighting (kWh)'].astype(str) + '%'
ahs_reduction_pct['HS DG Gym (kWh)'] = ahs_reduction_pct['HS DG Gym (kWh)'].astype(str) + '%'  # adds the dollar sign and percent sign back to the data
ahs_reduction_pct['HS Kitchen Emergency (kWh)'] = ahs_reduction_pct['HS Kitchen Emergency (kWh)'].astype(str) + '%'
ahs_reduction_pct['HS M1 Chillers (kWh)'] = ahs_reduction_pct['HS M1 Chillers (kWh)'].astype(str) + '%'
ahs_reduction_pct['HS CC Collins Center (kWh)'] = ahs_reduction_pct['HS CC Collins Center (kWh)'].astype(str) + '%'

ahs_reduction_diff['HS Main (kWh)'] ='$' + ahs_reduction_diff['HS Main (kWh)'].astype(str)
ahs_reduction_diff['LV Plug Loads (DHB)'] = '$' +  ahs_reduction_diff['LV Plug Loads (DHB)'].astype(str)
ahs_reduction_diff['HS DL Lighting (kWh)'] = '$' + ahs_reduction_diff['HS DL Lighting (kWh)'].astype(str)
ahs_reduction_diff['HS DG Gym (kWh)'] = '$' + ahs_reduction_diff['HS DG Gym (kWh)'].astype(str)
ahs_reduction_diff['HS Kitchen Emergency (kWh)'] = '$' +  ahs_reduction_diff['HS Kitchen Emergency (kWh)'].astype(str)
ahs_reduction_diff['HS M1 Chillers (kWh)'] = '$' + ahs_reduction_diff['HS M1 Chillers (kWh)'].astype(str)
ahs_reduction_diff['HS CC Collins Center (kWh)'] = '$' + ahs_reduction_diff['HS CC Collins Center (kWh)'].astype(str)




ahs_energy = pd.read_csv(r"C:\Users\shrey\OneDrive\Documents\5 Programming\Energize\Learning Pandas\2016-2019 - AHS Daily (2300-0400)-Sample1.csv",
                         skiprows=4, usecols=range(8), header=None, names=['Date','HSKE','HSDG','LVPL','HSDL','HSM','HSCC','HSMC']) # imports the original data

ahs_energy["Date"]= pd.to_datetime(ahs_energy["Date"], errors ='coerce')
ahs_energy["HSKE"] = pd.to_numeric(ahs_energy.HSKE, errors='coerce')
ahs_energy["HSDG"] = pd.to_numeric(ahs_energy.HSDG, errors='coerce')
ahs_energy["LVPL"] = pd.to_numeric(ahs_energy.LVPL, errors='coerce')
ahs_energy["HSDL"] = pd.to_numeric(ahs_energy.HSDL, errors='coerce')
ahs_energy["HSM"] = pd.to_numeric(ahs_energy.HSM, errors='coerce')
ahs_energy["HSCC"] = pd.to_numeric(ahs_energy.HSCC, errors='coerce')
ahs_energy["HSMC"] = pd.to_numeric(ahs_energy.HSMC, errors='coerce')
#makes the data a float instead of object to find the total energy for each day

ahs_energy['Year'] = ahs_energy['Date'].dt.year # makes a year column to seperate the data into seperate years
ahs_energy_day_year1= ahs_energy[ahs_energy['Year'] == 2016]
ahs_energy_day_year2= ahs_energy[ahs_energy['Year'] == 2018]  # calcuates the total energy saved and the money savings
Energy_reduction = ahs_energy_day_year1['HSM'].sum() - ahs_energy_day_year2['HSM'].sum()
Energy_saving =  Energy_reduction*0.16


text1 = pd.DataFrame({'Average percent change over 2016'})
text2 = pd.DataFrame({'Average savings over 2016'})


ahs_energy_csv = open("averageEnergyReport.csv","w+")  # writes all the data to a csv
ahs_energy_csv.write("Electricity used by AHS between 23:00 hrs and 4:00 hrs\nTotal yearly saving over 2016: $" + str(Energy_saving)+"\nkWh Saved since 2016: "+str(Energy_reduction)+"\n\n")
ahs_energy_Data.to_csv("averageEnergyReport.csv", sep=',', index= False)
ahs_energy_csv.close()

with open('averageEnergyReport.csv', 'a') as f:
    text1.to_csv(f, index=False, header=False)

with open('averageEnergyReport.csv', 'a') as f:
    ahs_reduction_pct.to_csv(f, index=False)

with open('averageEnergyReport.csv', 'a') as f:
    text2.to_csv(f, index=False, header=False)

with open('averageEnergyReport.csv', 'a') as f:
    ahs_reduction_diff.to_csv(f, index=False)