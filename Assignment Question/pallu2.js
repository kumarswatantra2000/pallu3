function addUniqueItem(arr, item) {
    if (!arr.includes(item)) {
      arr.push(item);
    }
  }
  
  // Example usage
  const uniqueFruits = [];
  addUniqueItem(uniqueFruits, "apple");
  addUniqueItem(uniqueFruits, "banana");
  addUniqueItem(uniqueFruits, "apple");
  console.log(uniqueFruits); // ["apple", "banana"]
  