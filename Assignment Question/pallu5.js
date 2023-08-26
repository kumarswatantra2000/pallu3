function findMinMax(arr) {
    let min = arr[0];
    let max = arr[0];
    
    for (let i = 1; i < arr.length; i++) {
      if (arr[i] < min) {
        min = arr[i];
      }
      
      if (arr[i] > max) {
        max = arr[i];
      }
    }
    
    return [min, max];
  }
  
  // Example usage
  const numbers = [2, 7, 1, 9,8];
  const [min, max] = findMinMax(numbers);
  console.log(`Min: ${min}, Max: ${max}`); // Outputs "Min: 1, Max: 9"
  