# Data_Pipelines_on_the_Cloud

the project is described in the following medium article
[Data Engineering Blog Post](https://medium.com/p/d98ede61ed12 "Data Engineering Blog Post")

##CaseStudy: Gans
Gans is a startup developing an e-scooter-sharing system. It aspires to operate in the most populous cities all around the world. In each city, the company will have hundreds of e-scooters parked in the streets and allow users to rent them by the minute.



Some of Gans’ most notorious and well-established competitors are TIER, probably the biggest player in the German-speaking countries, now expanding throughout other European countries, and Bird, a cool Californian company, already established in Europe.

The focus of most e-scooter companies is sustainable mobility: they are on the good side of the dichotomy between Battery Electric Vehicles (BEV) versus Internal Combustion Engine Vehicles (ICEV). Most of their marketing efforts push the eco-friendly narrative: this is how they acquire new users and gain good press from citizens encountering scooters around the city.

However, Gans has seen that its operational success depends on something more mundane: having its scooters parked where users need them.

Ideally, scooters get rearranged organically by having certain users moving from point A to point B, and then an even number of users moving from point B to point A. However, some elements create asymmetries. Here are some of them:

In hilly cities, users tend to use scooters to go uphill and then walk downhill.
In the morning, there is a general movement from residential neighbourhoods towards the city centre.
Whenever it starts raining, e-scooter usage decreases drastically.
Young tourists travelling with cheap flights are a big potential group of users, but they need to find scooters downtown or nearby touristic landmarks.
There are some actions that the company can perform to solve these asymmetries, namely:

Use a truck to move scooters around.
Create economic incentives for users to pick up or leave scooters in certain areas, as the image below shows.


Either way, the company wants to anticipate as much as possible scooter movements. Predictive modelling is certainly on the roadmap, but the first step is to collect more data, transform it and store it appropriately. This is where you come in: your task will be to collect data from external sources that can potentially help Gans predict e-scooter movement. Since data is needed every day, in real-time and accessible by everyone in the company, the challenge is going to be to assemble and automate a data pipeline in the cloud.

