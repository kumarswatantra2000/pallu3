const obj1 = {1: "s", 2: "w"}
const obj2 = {3: "e", 4: "t"}
const obj4 = {5: "t", 6: "r"}

//const obj3 = { obj1, obj2}
//onst obj3 = object.assign({}, obj1, obj2)
const obj3 = {...obj1[1],...obj2 }
console.log(obj3)