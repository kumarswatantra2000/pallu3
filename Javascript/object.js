// singleton

//object literals

const jsuser = {
    name: "swatantra",
    "full name": "swatantra kumar rajak"
    [mySym]: "mykey1",
    age: 22,
    location: "patna",
    email: "swatantrakumar0220@gmail.com",
    isLoggedIn: false,
    lastLoginDays:["Monday", "Saturday"]
}

console.log(JsUser.email);
console.log(JsUser["email"])
console.log(jsUser["full name"])
console.log(typeof JsUser.mySym)

JsUser.email = "swatantra@gmail.com"
Object.freeze(jsUser)
JsUser.email = "swatnntra@gmail.com"
console.log(JaUser);