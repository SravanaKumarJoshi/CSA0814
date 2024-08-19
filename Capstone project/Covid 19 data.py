import requests

url = "https://disease.sh/v3/covid-19/countries/india"

response = requests.get(url)
data = response.json()

# Accessing the data
cases = data["cases"]
deaths = data["deaths"]
recovered = data["recovered"]

# Printing the data
print("COVID-19 Statistics for India:")
print("-------------------------------")
print(f"Cases today: {data['todayCases']}")
print(f"Deaths today: {data['todayDeaths']}")
print(f"Recovered today: {data['todayRecovered']}")
print(f"Active cases: {data['active']}")
print(f"Critical cases: {data['critical']}")
print(f"Cases per million: {data['casesPerOneMillion']}")
print(f"Deaths per million: {data['deathsPerOneMillion']}")
print(f"Tests done: {data['tests']}")
print(f"Tests per million: {data['testsPerOneMillion']}")
print(f"Total cases: {cases}")
print(f"Total deaths: {deaths}")
print(f"Total recovered: {recovered}")
