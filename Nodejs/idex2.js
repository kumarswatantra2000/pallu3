const http = require('http');

const PORT = 2365;
const HOSTNAME = 'localhost';

const server = http.createServer((req, res) => {
    res.end('node Server create by swatantra kumar!');

});

server.liisten(PORT, () =>{
    console.log('Server running at ${HOSTNAME}:${PORT}');
})
