# Pesix 
<p align="left">
    <a href="LICENSE" alt="License">
        <img src="https://img.shields.io/badge/License-MIT-brightgreen.svg" /></a></p>

![Ranked](https://img.shields.io/badge/LA%20Hacks%202019-Best%20Social%20Hack-green)

        
Reduce your carbon footprint and earn rewards for it.

---------------
## Inspiration
Carbon emission is a well known threat to the environment and still *How many people try becoming more environmental friendly even after being aware of the consequences?*

## What it does
It allows you to easily pay your bills and track your carbon footprint while *earning* rewards seamlessly using Amazon Alexa.

## How we built it

We built a skill for Amazon Alexa using their developer console and used Amazon lambda services to deploy it and seamlessly connect it with the web server. Bills for the scheduled payments are generated using Nessie, Capital One's API and the transaction is monitored by the platform to calculate carbon emission. We used ethereum framework to monitor the carbon emission by each individual and maintain a leaderoard which later determines the reward of the individuals. The web-app made with HTML5 and graph.js also provides analytics for every user's carbon footprint. We used node.js for backend and integration with the ethereum framework.

## Website
```
http://www.pesix.com/
```

## Project setup
```
npm install
```

#### Compiles and hot-reloads for development
```
npm run serve
```

#### Compiles and minifies for production
```
npm run build
```

#### Run your tests
```
npm run test
```

#### Lints and fixes files
```
npm run lint
```

#### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
