// Create an object to represent the store's inventory
const inventory = {
    products: [
      { name: "Product 1", price: 10.99, quantity: 100 },
      { name: "Product 2", price: 19.99, quantity: 50 },
      { name: "Product 3", price: 5.99, quantity: 200 }
    ],
  
    // Function to add a product to the inventory
    addProduct: function(name, price, quantity) {
      const newProduct = { name, price, quantity };
      this.products.push(newProduct);
      console.log(`Added ${quantity} of ${name} to inventory.`);
    },
  
    // Function to remove a product from the inventory
    removeProduct: function(name) {
      const index = this.products.findIndex(product => product.name === name);
      if (index !== -1) {
        this.products.splice(index, 1);
        console.log(`Removed ${name} from inventory.`);
      } else {
        console.log(`Product ${name} not found in inventory.`);
      }
    },
  
    // Function to update the quantity of a product in the inventory
    updateQuantity: function(name, quantity) {
      const product = this.products.find(product => product.name === name);
      if (product) {
        product.quantity = quantity;
        console.log(`Updated quantity of ${name} to ${quantity}.`);
      } else {
        console.log(`Product ${name} not found in inventory.`);
      }
    },
  
    // Function to list all products in the inventory
    listProducts: function() {
      console.log("Current inventory:");
      this.products.forEach(product => {
        console.log(`${product.name} - $${product.price} - Quantity: ${product.quantity}`);
      });
    }
  };
  
  // Example usage of the inventory feature
  inventory.listProducts(); // List all products in the inventory
  inventory.addProduct("Product 4", 7.99, 150); // Add a new product to the inventory
  inventory.updateQuantity("Product 1", 50); // Update the quantity of a product
  inventory.removeProduct("Product 2"); // Remove a product from the inventory
  inventory.listProducts(); // List all products in the inventory again
  