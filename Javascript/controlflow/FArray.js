function swatantraKumar(number){
    return function (num) {
        return number.includes(num);
    };
}
const arr = [1,2,3,4,56,7,8];
const palluNum = swatantraKumar(arr);
console.log(palluNum(3));
console.log(palluNum(5));