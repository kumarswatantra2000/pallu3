function getRandomElement(arr) {
    const randomIndex = Math.floor(Math.random() * arr.length);
    return arr[randomIndex];
  }
  
  // Example usage
  const fruits = ["apple", "banana", "orange", "kiwi", "grape"];
  const randomFruit = getRandomElement(fruits);
  console.log(randomFruit); // Outputs a random fruit from the array
  