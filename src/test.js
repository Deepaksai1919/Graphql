const fs = require('fs');
let data = fs.readFileSync('./schema/types.graphql', 'utf-8');

console.log(data)