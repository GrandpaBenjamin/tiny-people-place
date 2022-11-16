const http = require("http");
const CronJob = require('cron').CronJob;
//const World = require('./world.cjs').World;

class World {
    constructor(name,startingPopulation) {
        this.name = name;
        this.startingPopulation = startingPopulation;
    }

    tick(){
        console.log("tick")
    }
}

const host = "localhost";
const port = 8000;

/*
var job = new CronJob(
	'* * * * * *',
	function() {
		currentMessage
	},
	null,
	true,
	'Europe/London'
);
*/

const theWorld = new World("earth",2);
setTimeout(theWorld.tick, 10, "some message");

const request = function (req, res) {
    res.setHeader("Content-Type", "text/plain");
    switch (req.url) {
        case "/":
            res.setHeader("Content-Type",'app')
            res.writeHead(200);
            res.end("hello, you seem lost.\ntry one of theses urls:\n\n/status\n/world\n/api");
            break
        case "/favicon.ico":
            res.writeHead(200);
            res.end("eat shit and die");
            break
        default:
            res.writeHead(404);
            res.end(JSON.stringify({error:"Resource not found"}));
    }
};

const server = http.createServer(request);
server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});