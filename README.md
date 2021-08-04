
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


## **Day = 1 (31.07.2021)**
I started to handle with the data I collected yesterday. None values and the data with no standard is a big problem. Today I worked on them about 2 hours. But there is more to do. None and nan are not acting same. I understood this so bad.
- Making metrics standard
  - cm, mm, or meters,
  - screen resolutions 27'', 27' , 27 inch or 27INCH,
  - freedos, dos or FreeDOS
[sample code](https://github.com/bilative/x-days-of-code/blob/master/code_pieces/day01_datamanipulation.py)  here.

![fiats](https://user-images.githubusercontent.com/70684994/127753022-ccbcac36-88b4-4720-aa0e-3e317d186c22.png)

## **Day 2 (01.08.2021)**
I solved some hackerrank problems and I read "Yapay Zeka Uygulamalari (4th edition)" from Prof. Dr. Cetin Elmas. Actually I bought thos book couple weeks ago, and today I have started to read it and apply. I refreshed my knowledges and I started to learn some mores.

![0000000381159-1](https://user-images.githubusercontent.com/70684994/127784707-67503231-bcc6-41bb-a543-eb69ad114e97.jpg)

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

## **Day 4 (03.08.2021)**
After working day, I didn't do something important today.
* I attended to lesson of my course and we examined use cases of cassandra and some other NoSQL dbs.
* I solved little details around my data that I web scraped from online sales website. I'll start to analyze in couple days.

## **Day 5 (04.08.2021)**
If I wanna have data engineering skills, I think I should improve my level of knowledge in REST API. And actually I'm having fun while handling with html procedures.
- I took some steps about how can I create a token in my APIs, and How can I verified users.
- I used Flask for APIs, and JWT.