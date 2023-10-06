// primitive

// 7 types : string, number, boolean, null, undifined,symbol, BigInt

//const score = 100
//const scoreValue = 100.3

//const isLoggedId = false
//const outsideTemp = null
//let userEmail;

//const id = Symbol('123')
//const anotherId = Symbol('123')

//console.log(id == anotherId);
//const bigNumber = 3256145544587n

// reference (non premitive)

// Array, object , Functions

//cnst heros = ["swatantra","kumar","hitesh"]
//let myObj = {
  //  name : "swatantra",
    //age: 22,
//}
//const myFunction = function(){
  //  console.log("hello world");
//}

//console.log(typeof bigNumber);

//memory type of two
// stack (primitive), heap (Non-primitive)

//let myYoutubename = "kumarswatantrarajak"

//let anothername = myYoutubename
//anothername = "kumarswatantra"
//console.log(anothername);
//console.log(another);

let userone = {
    email:  "pkpallu0220@gmail.com",
    upi: "user@ybl"
}

let userTwo = userone
userTwo.email = "kumar@gmail.com"

console.log(userOne.email);
console.log(userTwo.email);