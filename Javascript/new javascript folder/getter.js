class Usser {
    constructor(email, password){
        this.email = email;
        this.password = password
    }
    get email(){

    }
    get password(){
        return this.password.toUpperCase()
    }
    set password(value){
        this._password = value.toUpperCase()
    }
}
const swatantra = new UserActivation("swatantra123@gmail.com", "993940")
console.log(swatantra, password);