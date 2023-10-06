//const marvel__heros = ["thor","Iroman","spiderman"]
//const dc_heros = ["swatantra","flash","batman"]

//marvel__heros.push(dc_heros)

//console.log(marvel_heros);

//const all_new_heros = [...marvel_heros, ...dc_heros]
//console.log(all_new_heros)

const another_array = [1,2,3, [4,5,6], 7, [6,7,[4, 5]]]

const real_another_array = another_array.flat(Infinity)
console.log(real_another_array);
console.log(Array.isArray("swatantra"))
console.log(Array.from("swatantra"))
//console.log(Array.from({name: "swatantra"}))//Intersting array 
let score1 = 123
let score2 = 234
let score3 = 567
console.log(array.of(score1, score2,score3));