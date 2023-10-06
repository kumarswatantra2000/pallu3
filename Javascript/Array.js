//Array

const myArr = [0,1,2,3,4,5,5,6,7]
const myHeros = ["swatantra","kumar"]

const myArr2 =  new Array(1,2,34,56)
//console.log(myArr[1]);
//console.log(myHeros[2]);

//Array method

//myArr.push(6)
//myArr.push(7)
//myArr.pop(9)
//yArr.unshift(9)
//myArr.shift()
//console.log(myArr.includes(10));
//console.log(myArr.indexOf(3));
//const newArr = myArr.join()
//console.log(myArr);
//console.log( newArr)


// slice, splice

console.log("a ", myArr);

const myn1 = myArr.slice(1,3)

console.log(myn1);
console.log("b ", myArr);

const myn2 = myArr.splice(1, 3)
console.log("c",myArr);
console.log(myn2);

