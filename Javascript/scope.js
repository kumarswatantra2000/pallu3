//var c = 300
let a = 300
if (true) {
    let a = 10
    const b = 20
  //  console.log("INNER: ", a);

}
//console.log(a);
//console.log(b);
//console.log(c);

//NESTED SCOPE

function one(){
    const username = "swatantra"
    function two(){
        const website = "pw skills"
        console.log(username)
    }
    //onsole.log(website);
   // two()

}
//one()

if (true) {
    const username = "swatantra"
    if (username=== "swatantra") {
        const website = " pw skills"
        //console.log(username + website);
    }
    //comsole.log(website)
}

//console.log(username);
 

//******************interestiong**********

console.log (addone(5));

function addone(num){
    return num + 1
}


const addtwo =function(num){
    return num + 2

}
addtwo
