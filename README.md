# Django Global IOT Dashboard

IoT Devices all over world sends real time data to Dashboard

#Installation Instruction 

| RPI (Raspbian) | Linux ( Ubuntu)|
| ------------- | ------------- |
| [Postgres for RPI](https://pimylifeup.com/raspberry-pi-postgresql/)  | [Postgres for Ubuntu](https://ubuntu.com/server/docs/install-and-configure-postgresql)  |
| [Apache For RPI](https://pimylifeup.com/raspberry-pi-apache/)  | [Apache for Ubuntu](https://ubuntu.com/tutorials/install-and-configure-apache#1-overview)  |

For required libraries and additional software for GIS data, we added requirements.txt file and Software installation links in below this line, you just to follow this command.

You have to install GeoDjango here is some link:-

    1. https://docs.djangoproject.com/en/3.0/ref/contrib/gis/install/geolibs/
    2. https://www.postgresql.org/download/
    3. https://realpython.com/location-based-app-with-geodjango-tutorial/
    4. https://docs.djangoproject.com/en/3.0/ref/contrib/gis/tutorial/#setting-up
    5. Setup postgresql gis database and add username and password in setting file

```
pip install -r requirements.txt

```

Run some command for running the Project:

```
1. python manage.py makemigrations

```
```
2. python manage.py migrate

```
```
3. python manage.py runserver

```
=======

Steps to Execute

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py runserver`

![](IoTGlobal.png)

![](iotglobal1.PNG)

![](iotglobal2.PNG)

![](IOT1.PNG)

![](IOT2.PNG)


![](flow.png)

Here is references of IoT Devices:-
 1. https://builtin.com/articles/iot-devices
 2. https://www.techtarget.com/iotagenda/definition/IoT-device
 3. https://www.leorover.tech/post/raspberry-pi-or-arduino-when-to-choose-which
