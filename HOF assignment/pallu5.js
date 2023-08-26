function isValidUrl(url) {
    const pattern = /^(https?:\/\/)?[\w-]+\.[\w-]+\S*$/;
    return pattern.test(url);
  }
  
  // Example usage
  console.log(isValidUrl("https://www.example.com")); // true
  console.log(isValidUrl("http://www.example.com")); // true
  console.log(isValidUrl("www.example.com")); // true
  console.log(isValidUrl("example.com")); // true
  console.log(isValidUrl("https://www.example.com/path")); // true
  console.log(isValidUrl("https://www.example.com/path?query=string")); // true
  console.log(isValidUrl("ftp://www.example.com")); // false
  console.log(isValidUrl("www.example")); // false
  console.log(isValidUrl("example")); // false
  console.log(isValidUrl("https://www.example.com/ path")); // false
  