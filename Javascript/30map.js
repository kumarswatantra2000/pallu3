const pallunum = [1,2,3,4,5,6,7,8,9,10]
//const swatantrauser = pallunum.map( (num) => { return num +5})
//const swatantrauser = pallunum.map( (num) => num + 10)

const swatantrauser = pallunum
.map( (num) => num *10 )
.map( (num) => num +1)
.filter( (num) => num  >= 50)
console.log("swatantrauser");