function sayHello() {
    let name = "John"; // Function variable
  
    if (true) {
        let message = "Hello"; // Block variable
        console.log(message + " " + name); 
        // Output: "Hello John"
    }
  
    console.log(message); 
    // Output: Uncaught ReferenceError: 
    // message is not defined
}
  
sayHello();