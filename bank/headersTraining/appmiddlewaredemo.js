"use strict";
const express = require('express');
const app = express();

const { sup, how } = require("./myMiddleware")

//app.use(sup); // this will handle every single call. this is great when u first start but we don'tt have to handle on every call. lets use app.get()
app.get("/", (req, res) => {
    res.send({data:'what up saenchi!S'})
})


app.listen(4000, err => {
    if (err) {
        console.log("there was a problem loading server", err);
        return;
    }
    console.log('Listtening on port 4000')
});