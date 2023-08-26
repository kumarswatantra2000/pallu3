function swapValues(a, b) {
    [a, b] = [b, a];
    console.log(`a = ${a}, b = ${b}`);
  }
  
  // Example usage
  let x = 1;
  let y = 2;
  console.log(`x = ${x}, y = ${y}`);
  swapValues(x, y);
  console.log(`x = ${x}, y = ${y}`);
  