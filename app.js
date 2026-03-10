const express = require("express");
const app = express();
const http = require("http");
const server = http.createServer(app);
//server.maxRequestsPerSocket = 1;
app.use(express.static("public"));
console.log("Hello");
app.listen(3000, (req, res) => {
  console.log("I am Listening");
});
//change 1 
//conflict aega