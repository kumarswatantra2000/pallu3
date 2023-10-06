const descripter = Object.getOwnPropertyDescriptor(Math, "PI")
//console.log(descripter);


//console.log(Math.PI)
//Math.PI = 5
//console.log(Math.PI);



//const cahi = Object.create(null)

const cahi = {
    name: 'swatantra kumar',

    price: 250,

    isAvailable: true

}
//console.log(Object.getOwnPropertyDescriptor(chai, "name"));



//Object.defineProperty(chai, 'name', {
  //  writable: false,
    //enumerable: false

//})
//sconsole.log(Object.getOwnPropertyDescriptor(chai, "name"));

for (let [key, value] of object.enterise(chai)){
    if (typeof value !== 'function') {
        console.log('${key} : ${value}');
    }

    }
    //console.log('${key} : ${value}');
}