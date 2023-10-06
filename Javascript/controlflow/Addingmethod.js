function Swatantra(name) {
    this.name = name;
}
Swatantra.prototype.printDetails = function () {
    console.log('hello, my name is ${this.name}');
};
const swatantra = new Swatantra("pallu");
swatantra.printDetails();