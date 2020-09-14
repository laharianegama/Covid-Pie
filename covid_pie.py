from covid import Covid
import sys
import matplotlib.pyplot as plt

covid = Covid()
countries = covid.list_countries()
Country_name=input("ENTER THE COUNTRY NAME:  ").capitalize()


#get the country's virus data
virus_data=covid.get_status_by_country_name(Country_name)
print(virus_data)

#save data related to confirmed cases for the future reference
Active_cases=virus_data['confirmed']

#remove unnecesary values like latitude longitude,lastupdate
remove=['id','country','latitude','longitude','last_update','confirmed']

for i in remove:
    virus_data.pop(i)

#virusdata is dictionary data type
#we should split them as keys and values respectively

id=list(virus_data.keys())
value=[str(i) for i in virus_data.values()]


#piechart creation
plt.pie(value,labels=id,colors=['r','yellow','g'] ,autopct='%1.1f%%')
plt.title("COUNTRY : "+Country_name.upper()+"\n TOTAL ACTIVE CASES :" +str(Active_cases))
plt.legend()
plt.show()
