const http = require("http");

const host = "localhost";
const port = 8000;

const request = function (req, res) {
    switch (req.url) {
        case "/":
            res.writeHead(200);
            res.end("hello, you seem lost.\ntry one of theses urls:\n\n/status\n/world\n/api");
            break
        case "/favicon.ico":
            res.writeHead(200);
            res.end("eat shit and die");
            break
    }
};

const server = http.createServer(request);
server.listen(port, host, () => {
    console.log(`Server is running on http://${host}:${port}`);
});