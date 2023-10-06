function calculateCartPrice(...num1){
    return num1
}
//console.log(calculateCartPrice(400,500,765))

const user = {
    username: "swatantra",
    price: 200

}

function handleobject(anyobject){
    console.log('username is  ${anyobject.username} and price is {anyobject.price}');
}
handleobject(user)

const mynewArray = [100,300,400,600]

function returnSecondValue(getArray){
    return getArray[2]
}
//console.log(returnSecondValue(mynewArray));

console.log(returnSecondValue([234,546,789,1000]));