class User {
    constructor(email, password){
        this.email = email;
        this.password = password
    }
    //get email(){

    //}
    get password(){
        return this._password.toUpperCase()
    }
    set password(value){
        this._password = value
    }
}
const swatantra = new User("swatantra123@gmail.com", "993940")
console.log(swatantra, password);