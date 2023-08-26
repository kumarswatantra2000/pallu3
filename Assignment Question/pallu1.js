function countOccurrences(arr) {
  const counts = {};
  for (let i = 0; i < arr.length; i++) {
    const element = arr[i];
    if (counts[element]) {
      counts[element]++;
    } else {
      counts[element] = 1;
    }
  }
  return counts;
}

// Example usage
const fruits = ["apple", "banana", "orange", "apple", "banana", "apple"];
const fruitCounts = countOccurrences(fruits);
console.log(fruitCounts); // { apple: 3, banana: 2, orange: 1 }
