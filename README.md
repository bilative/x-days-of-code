
## Hi
Actually most of my daily routine is going with coding around data science / data engineering. So I think that I can share some of them here.

* This is a hard 'find the x' question. And I think I wont find the x soon.
```python
for day in range(x):
    codeMore()
    andMore()
```

* The things I shared in this repo are only about what I search, waht I learn and what am I improving myself.
* I working on my side projects after working days and weekends. So frequency of the new things could may be low.
* Small steps are gonna be in this repo but big pictures is gonna be in their own repos. (I'll link them)
  
### **_Note: The codes I have shared are only sample of whole picture._**


---
---

## **Day 16 (12.08.2021)**
Actually today I did almost nothing. But I built my portfolio github-page. For now there is only main page but Im planing to carry this repo to here (https://bilative.github.io/xdaysofcode) in couple days. And I'll collect all my blog post here also. You can check it [here](https://bilative.github.io/).

## **Day 14-15 (14-15.08.2021)**
During these 2 days I made a end-to-end project.
Project and all the details are [here](https://github.com/bilative/weekend-end-to-end-ds-project)


## **Day 12 (12.08.2021)**
Today I deployed my [twitter-eartquake-bot](https://github.com/bilative/twitter-earthquake-bot) application on cloud linux machine. Normally I'm using linux with interface but on cloud machine there is no interface, so deploying steps required some new codes to write for me.
I learned usefull things today like:
- ssh connection to remote machine with windows command prompt (ssh my_user@my_ip)
- docker save and load image command to send saved image to remote machine
- scp command to send saved image to remote machine (scp windows_path/file.tar linux_user@linux_ip:/path)

- And at the same time I used cli connection to my docker container.

I used to do these with interface mostly, So today is so today has been a lot of fun for me.
And twitter bot is active now 7/24, if there is a earthquake bigger than 4, bot will tweet it by [my twitter account](https://twitter.com/bilallozdemir).


## **Day 11 (11.08.2021)**
Today I rent a cloud machine (linux) for 12 months. I had no so much experience with linux, I know some basics but I wanna do more. Today:
- I raised my machine,
- Created new user except root,
- Installed ubuntu GUI
    - And I removed it after couple hours. Bc there was a problem with speed, it was not clear to use (center of my machine is Germany, distance could be problem)
- Installed python and docker and tested it.


## **Day 10 (10.08.2021)**
Today I searched some Java apps. And I solved some entry level Java problems on Hackerrank.
I'm at the begining of the Java. But I'm taking small steps.
In short term maybe I wont be good at it but, in long term (maybe in 2 year) I know that I'll use it fluently. 


## **Day off (09.08.2021)**

## **Day 8 (07.08.2021)**
I study about REST Api more today.
* [This one](https://github.com/bilative/resty/tree/master/jsonPOST_functOutput) was one of my steps.
## **Day 9 (08.08.2021)**
Today I took a google cloud certification course.

## **Day 7 (06.08.2021)**
Today me and one of my friend checked my projects (smth like code review). And we decide that I can make my codes more efective.
* I redesigned some of my projects design to fit "Model Viev Controler".
* I eliminated repeated functions or lines. (for [example](https://github.com/bilative/bookstore-db-hw/blob/master/libs/inserts.py))

We decided to do code reviews more. In this way I'll improve my skills by perspective of other experts, and avoid from mistakes.

## **Day 6 (05.08.2021)**
Today I started to analyze the data I scraped online store. But after start to know data and analyze I realize that variation on independent variables are not enough. I was aim to predict Prices' of the products but prices are seem not continious variable to use regression. Im talking like this bc prizes are like 6499, 6999, 7499...
* There are about 3600 product but there is 18 different price labels.
* So this is smth like classification problem, and I dont find smth true to use regression or classification in this situation.

I'll try smth different later.

## **Day 5 (04.08.2021)**
If I wanna have data engineering skills, I think I should improve my level of knowledge in REST API. And actually I'm having fun while handling with html procedures.
- I took some steps about how can I create a token in my APIs, and How can I verified users.
- I used Flask for APIs, and JWT.

## **Day 4 (03.08.2021)**
After working day, I didn't do something important today.
* I attended to lesson of my course and we examined use cases of cassandra and some other NoSQL dbs.
* I solved little details around my data that I web scraped from online sales website. I'll start to analyze in couple days.


## **Day 3 (02.08.2021)**
Today I study on MongoDB in the course I take. Actually I'm using mongoDB in office everyday but I'm mostly using it on my apps to store images. In the course mostly we study on tabular data. It was good, and enjoyful.

And today I solve some problem in an exam. There was an sql question in the exam, and it was smth like this:

![asd](https://user-images.githubusercontent.com/70684994/127983336-5edbc7fe-140a-4603-981d-62e3f6f39aa6.png)

- _There are 2 table as above. And show us the people who talked on the phone less than or equal to 15 minutes._
  - _This is good because I didnt face with a problem required 1 vs 2 Inner Join like this. And I didnt know that this is possible._
  - _But my solution was correct, it was smth like this:_
```
SELECT TABLE2.name FROM TABLE2
    INNER JOIN TABLE1 ON TABLE2.phone_number = TABLE1.caller OR TABLE2.phone_number = TABLE1.callee
        GROUP BY TABLE2.name
        HAVING sum(calls.total_time) <= 15
            ORDER BY TABLE2.name
```

## **Day 2 (01.08.2021)**
I solved some hackerrank problems and I read "Yapay Zeka Uygulamalari (4th edition)" from Prof. Dr. Cetin Elmas. Actually I bought thos book couple weeks ago, and today I have started to read it and apply. I refreshed my knowledges and I started to learn some mores.

![0000000381159-1](https://user-images.githubusercontent.com/70684994/127784707-67503231-bcc6-41bb-a543-eb69ad114e97.jpg)

## **Day = 1 (31.07.2021)**
I started to handle with the data I collected yesterday. None values and the data with no standard is a big problem. Today I worked on them about 2 hours. But there is more to do. None and nan are not acting same. I understood this so bad.
- Making metrics standard
  - cm, mm, or meters,
  - screen resolutions 27'', 27' , 27 inch or 27INCH,
  - freedos, dos or FreeDOS
- [sample code](https://github.com/bilative/x-days-of-code/blob/master/code_pieces/day01_datamanipulation.py)  here.

![fiats](https://user-images.githubusercontent.com/70684994/127753022-ccbcac36-88b4-4720-aa0e-3e317d186c22.png)

## **Day = 0 (30.07.2021)**
In last days I spent my time to find a topic and a good website to do web scraping. And today i collected some of them from a online sales website. I wanna make a end to end data science project, so this one is first step.
I collected data about phones, laptops, all in one pcs' and tablets. Now I have a real world dataset with more than 5k rows. Now there is so much things to do like cleaning/ standardizing.
- I followed a path like:
  - Taking urls of whole pages 
  - Taking urls of whole products on each pages
  - Taking features and values of all products
- I took 5k+ rows of data and more than 150 features.
- [sample code](https://github.com/bilative/x-days-of-code/blob/master/code_pieces/day00_scraping.py)

![repp](https://user-images.githubusercontent.com/70684994/127746179-41232d32-a9bb-4013-9f1d-e9c8577cb2f3.png)


