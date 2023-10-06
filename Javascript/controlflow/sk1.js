class swatantra {
    constructor(name = "Unknow",age = 0) {
        this.name = name;
        this.age = age;
    }
    getDetails() {
        return 'name: ${this.name}, Age: ${this.age}';
    }
}
const pallu1 = new swatantra("kumar", 20);
console.log(pallu1.getDetails());
const pallu2 = new swatantra();
console.log(pallu2.getDetails());