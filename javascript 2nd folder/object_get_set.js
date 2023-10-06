const User = {
    _email: 'swatantrakumar234@gmail.com',
    _password: "8247586958",



    get email(){
        return this._email.toUpperCase()
    },

    set email(value){
        this._email = value
    }

}
const tea = Object.create(User)
console.log(tea._password);