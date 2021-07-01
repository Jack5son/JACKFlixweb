@echo off

 call .\showsenv\Scripts\activate
cd jackflixweb
python manage.py runserver
pause
