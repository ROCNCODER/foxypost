
# foxypost
![foxypost](/logo.jpg)

__The project is aimed at creating an abstraction over popular libraries for obtaining data from posts from various social media__ 
<br/>
Проект направлен на создание абстракции над популярными библиотеками получения данных с постов из различных социальных медиа
<br/>


__Facebook instagramming is currently available for the library to receive data from Facebook and Instagram__
<br/>
На данный момент библиотека способна получать данные из instagram


__To work, install libraries__
<br/>
Для работы установить библиотеки


```
pip install - r requirements.txt
```

## Masterminds

[https://github.com/kevinzg/facebook-scraper](https://github.com/kevinzg/facebook-scraper)
<br/>
[https://github.com/adw0rd/instagrapi](https://github.com/adw0rd/instagrapi)
<br>

__Expected changes and problems__<br>
Ожидаемые изменения и проблемы<br>

- [ ] Solve problems with storing temporary data in a single file <br>Решить проблемы с хранением временных данных в едином файле
- [ ] Remember to format output data from the street under dictation for work in the production shop <br> Поменять формат выходных данных с str на dict для удобства работы производного софта
- [ ] Configure the work of the framework working with facebook <br>Настроить работу библиотеки работающий с facebook
- [ ] Add new social media <br> Добавить новые социальные медиа
- [ ] Create a general scheme for generating input data for more precise work settings <br>Создать общую схему формирования входных данных для более точной настройки работы

## instagram

__Since at the moment the library selected for collecting statistics from Instagram posts is experiencing problems. A proprietary solution based on selenium and selenium-wire was written. It requires saving posts in folders that are located in the saved instagram tab. And send the program a link to this folder, as well as the username and password from the account where the folder is located.__<br>
Так как на данный момент библиотека выбранная для сбора статистики с постов в инстаграм испытывает проблемы. Было написано собственное решение на базе selenium и selenium-wire. Для него требуется сохранять посты в папках , которые находятся во вкладке сохранённые инстаграм. И передавать программе ссылку на эту папку, а так же логин и пароль от аккаунта где находится папка.