import express from "express";
let hole1 = 300;


const server = express();
const port = 3000;

server.get('/', (req, res) => {
    res.send("Welcome to Virtual Disc Golf\n\n1.) Driver (D)\n2.) Mid-Range (M)\n3.) Putter (P)")
})

server.listen(port, function () {
    console.log('Listening on ' + port);
});



// let disc = prompt("What disc would you like to use?: ");
