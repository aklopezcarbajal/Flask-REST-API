# Flask REST API

Simple REST API built in python using Flask.

It supports the requests <b>get</b>, <b>put</b>, <b>patch</b> and <b>delete</b>. This API pulls data from a local SQL-Alchemy database of Animal Crossing villagers. 
The data set includes the villager's name, species, personality and quote.
The request '/villager/name' returns the villager's information in json format. 

## Running the application

In the command line, navigate to the folder where main.py is located. Then type:
```bash
# run the flask application
python main.py
```

Use your web browser to see the application running at http://127.0.0.1:5000/.

<img src="/img/home_page.png" alt="Home page" width="500" height="200"/>

Response example:

<img src="/img/request_example.png" alt="Request" width="450" height="200"/>

Run test.py to see all the supported requests in action. 
While the main application is still running, on a new command line type:
```bash
# test all the supported requests
python test.py
```

## Database

You can find the following characters:
<ol>
  <li>Muffy</li>
  <li>Rocket</li>
  <li>Bud</li>
  <li>Jitters</li>
  <li>Kidd</li>
  <li>Raymond</li>
  <li>Molly</li>
  <li>Lily</li>
  <li>Peanut</li>
  <li>Sprinkle</li>
</ol>
