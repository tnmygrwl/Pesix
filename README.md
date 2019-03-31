# pesix
Track your carbon footprint seamlessly

time's are changing, and it's time to change
# Pesix
## Inspiration
Carbon emission is a well known threat to the environment and still *How many people try becoming more environmental friendly even after being aware of the consequences?*

## What it does
It allows you to easily pay your bills and track your carbon footprint while *earning* rewards seamlessly using Amazon Alexa.

## How we built it

We built a skill for Amazon Alexa using their developer console and used Amazon lambda services to deploy it and seamlessly connect it with the web server. Bills for the scheduled payments are generated using Nessie, Capitol One's API and the transaction is monitored by the platform to calculate carbon emission. We used ethereum framework to monitor the carbon emission by each individual and maintain a leaderoard which later determines the reward of the individuals. The web-app made with HTML5 and graph.js also provides analytics for every user's carbon footprint. We used node.js for backend and integration with the ethereum framework.

## Challenges we ran into

Some of the challenges we ran into were:
<ol>
<li> Deciding on a concrete idea.</li>
<li>Deploying it on amazon Alexa and integrating it with the frontend. </li>
<li>Configuring Metamask with the web-app.</li>
<li>WiFi and network issues. </li>
</ol>

## Accomplishments that we're proud of

Gamifying an environmental problem to improve sustainability by incentivizing reduction of carbon emission through smart banking.

## What we learned

While the individual components work perfectly on their own, integrating it and *bringing* together the product as a whole is a huge challenge.

## What's next for Pesix
<ol>
<li>Scalaing the platform to calculate the carbon emission better</li>
<li>Providing it as B2B service.</li>
<li>And keep on asking *"What's Next?"*</li>
</ol>

## Our Website
```
http://www.pesix.com/
```

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
