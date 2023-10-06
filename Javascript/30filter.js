// Filter Map and reduce topic
//const coding = ["HTML","CSS","JAVASCRIPT","NODEJS","REACT.JS","PYTHON"]

//const values = coding.forEach( (item) => {
  //  console.log(item);
//} )

//console.log(values);

//const numMy = [1,2,3,4,5,6,7,8,9,10]
//const newpallu = numMy.filter( (numMy) => {
  //  return numMy > 6
//})
//const newpallu = []

//numMy.forEach( (num) => {
  //  if (numMy > 8){
    //    newpallu.push(numMy)
    //}
//})

//console.log(newpallu);

const pallu = [
    { title: 'book One',genre:'English', publish:1985,  edition: 2004},
    { title: 'book Two',genre:'science',publish: 190258,edition: 2309},
    { title: 'book Three',genre:'history', publish:19585,  edition: 205504},
    { title: 'book Four',genre:'math', publish:199885,  edition: 20034},
    { title: 'book Five',genre:'english', publish:195585,  edition: 203204},
    { title: 'book Six',genre:'hindi', publish:198785,  edition: 203204},
    { title: 'book Seven',genre:'science', publish:196585,  edition: 202504},
    { title: 'book eight',genre:'english', publish:19859,  edition: 200984},
];

const userpallu = pallu.filter( (pk) => pk.genre === 'english' )

userpallu = pallu.filter( (pk) => {return pk.publish >= 200000})
console.log(userpallu);

