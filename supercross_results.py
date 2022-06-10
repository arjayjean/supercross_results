import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import subprocess

subprocess.run('clear')


url = f'https://www.supercrosslive.com/results/current/2022/S2285/S1F1POINTS.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


rider_number = soup.find_all('td', {'data-title': '#'})
riders_number = [number.text for number in rider_number]


rider = soup.find_all('td', {'data-title': 'Rider'})
riders = [name.text for name in rider]

rounds = []

for i in range(1,18):
    results = soup.find_all('td', {'data-title': f'{i}', 'data-type': 'number'})
    round = [result.text for result in results]
            
    rounds.append(round)
    




