# Python-Data-Analytics
My projects in Data Analytics for the portfolio<br>
<br>
<b>PROJECT 1</b><br> 
Weather Report [view_code](weather-report.py)<br>
---GENERAL---<br>
In this project you can view,edit and add datas about weather. (Data are random).<br>
Data are in json-file [view_file](rdu-weather-history.json)<br>
---INFORMATION---<br>
This program display several values(date,minimum temperature, maximum temperature, 
precipitation,south-to-north water diversion,average daily wind speed) in entrys.<br>
There are buttons < and >, which allows viewing datas by each date.<br>
There are two modes(Search and Edit). Search mode allows searching any date entering data essential for you. To search, you need enter date, which is searched, then press Enter and essential data appear. If this date isn't in file or date is written wrongly, then error window will appear. Also in search mode all entrys except of date entry aren't editable.<br>
Edit mode allows editing any data, which after pressing Enter automatically save. If this data doesn't match necessary format, the error window will appear.<br>
There is a button Hint, where you can read information.<br>
There is a combobox, where you can search any data that are stored in file.<br>
<img width="871" height="405" alt="Image" src="https://github.com/user-attachments/assets/9493e649-873a-4e4e-8bc2-2999ae3d2bfd" />
<br>
There is a button Add, which allows adding new data. After pressing this button the window appears, where you can enter data in appropriate entrys.<br>
<img width="249" height="278" alt="Image" src="https://github.com/user-attachments/assets/caf39f37-3921-45e4-8455-f222b3aef8fe" />
<br>
There is a button Statistics, where you can see minimum temperature graphics of each year.To choose year, just click checkbutton with appropriate year<br>
<img width="618" height="322" alt="Image" src="https://github.com/user-attachments/assets/e84aecf6-c75d-4b10-8df9-03e15cfd7ce0" />
<br>
Also after using the program, json-file is updated.
---USED---<br>
-Tkinter<br>
-OOP<br>
