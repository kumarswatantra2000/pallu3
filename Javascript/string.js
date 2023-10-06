//const name = "swatantra"
//const repoCount = 50
//console.log(name + repoCount + "value");
//console.log('Hello my name is ${name} and my repo count is ${repoCount}');

const gameName = new String("swatan_tra")
//console.log(gameName._proto_);
//console.log(gameName.length);
//console.log(gameNmae.toUpperCase());
console.log(gameName.charAt(2));
console.log(gameName.indexOf('t'));

const newString = gameName.substring(0,5)
console.log(newString);

const anotherString = gameName.slice(-8,4)
console.log(anotherString);
const newStringOne =  "  swatantrasd"
console.log(newStringOne);
console.log(newStringOne.trim());

const url = "https://swatantrra.com/swatantra90rajak"
console.log(url.replace('%20', '-'))

console.log(url.includes('sunder'))
console.log(gameName.split('-'));