const user = {
    username: "swatantra",
    price: 999,

    welcomeMessage: function() {
     
        console.log ('${this.username} , welcome to website');
        console.log(this);   
    }
}

//user.welcomeMessage()
//user.username = "pallu"
//user.welcomeMessage()
//console.log(this);

//function pallu(){
  //  let username = "swatantra"
    //console.log(this.username);
//}
//pallu()

//onst pallu = function () {
  //  let username = "swatantra"
    //console.log(this.username);
//}
//arrow of function
//const pallu =  () => {
  //  let username = "swatantra"
    //console.log(this.username);
//}
//pallu()


//const addTwo = (num1, num2) => {
  //  return num1 + num2
//}
//emplyseet return
//explyseetly return

//const addTwo = (num1, num2) => ( num1 + num2)

const addTwo = (num1, num2) => num1 +num2
console.log(addTwo(3,4))


