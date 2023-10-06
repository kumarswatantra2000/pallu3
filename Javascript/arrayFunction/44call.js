function SetUsername(username){
    //complex Db class
    this.username = username
    console.log("called");
}

function createUser(usename, email, password){
    SetUsername.call(this, username)
    this.email = email
    this.password = password
}
const chai = new createUser("chai","chai@qwe.com", "123")
console.log(chai);