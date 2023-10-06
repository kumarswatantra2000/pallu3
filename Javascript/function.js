function sayMyName(){

    console.log("swatantra");
    console.log("pallu");
    console.log("rajak");
    console.log("vikash");
    console.log("mohan");
    console.log("gautam");
}

//sayMyName()

function addPallu(number1, number2){
    console.log(number1 + number2)

}
addPallu(6, 7)




function loginuserMessage(username){
    if(username == undefined){
        console.log("please enter a username");
        return
    }
    return '${username} just logged in'

}

//console.log(loginuserMessage("swatantra"))
console.log(loginuserMessage)