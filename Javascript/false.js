const userEmail = "kumarpallu0220@gmail.com"

if (userEmail) {
    console.log("Got user email");
} else {
    console.log("don't have user email");
}

// false values

//false, 0, -0, BigInt 0n, "", null, undefined, NaN

//truthy values
//"0","false"," ",[],{},function(){}

//if (userEmail.length === 0) {
  //  console.log("Array is empty");
//}

// Nullish Coalescing Operator (??): null ubndefined

let val1;
//val1 = 5 ?? 10
//val1 - null ?? 10
//val1 = undefined ?? 15
//val1 = nul ?? 10 ?? 20
//console.log(val1);

// Terniary Operator

//conditon ? true : false

const iceTeaPrice = 100
iceTeaPrice >= 80 ? console.log("less than 89"):console.log("more then 89")