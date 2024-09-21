const express = require('express')
const app = express()
const fetch = require('node-fetch')
const cors = require('cors')

// fetch("https://jsonplaceholder.typicode.com/todos/1").then(response => response.json()).then(json => console.log(json))
app.use(cors())

app.get('/mike', async (req,res) => {
    const response = fetch("https://jsonplaceholder.typicode.com/todos/1")

})