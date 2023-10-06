const shopingCarrt = [
    {
       itemName: "js course",
       price: 3000 
    },
    {
        itemName: "java course",
        price: 3500 
     },
     {
        itemName: "full stack webdevlopment course",
        price: 4000 
     },

     
     {
        itemName: "python course",
        price: 2000
     }
]
const priceToPay = shopingCarrt.reduce(( acc, item) => acc + item.price, 0)

console.log(priceToPay);
