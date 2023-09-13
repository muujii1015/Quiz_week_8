import sqlite3
import matplotlib.pyplot as plt


years = []
co2 = []
temp = []


conn = sqlite3.connect("climate.db")
cursor = conn.cursor()

cursor.execute("SELECT year, co2, temperature FROM ClimateData")
data = cursor.fetchall()

for row in data:
    years.append(row[0])
    co2.append(row[1])
    temp.append(row[2])


conn.close()



plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 

plt.tight_layout()  
plt.show()  
plt.savefig("co2_temp_1.png")  
