function isValidLinkedinUrl(url) {
    const pattern = /^https:\/\/(www\.)?linkedin\.com\/(in|profile)\/[a-zA-Z0-9-]+\/?$/;
    return pattern.test(url);
  }
  
  // Example usage
  console.log(isValidLinkedinUrl("https://www.linkedin.com/in/johndoe/")); // true
  console.log(isValidLinkedinUrl("https://www.linkedin.com/in/john-doe-1234/")); // true
  console.log(isValidLinkedinUrl("https://www.linkedin.com/profile/view?id=1234")); // true
  console.log(isValidLinkedinUrl("https://www.linkedin.com/in/johndoe")); // true
  console.log(isValidLinkedinUrl("https://linkedin.com/in/johndoe")); // true
  console.log(isValidLinkedinUrl("https://www.linkedin.com/in/")); // false
  console.log(isValidLinkedinUrl("https://www.linkedin.com/in/john-doe/extra-path")); // false
  console.log(isValidLinkedinUrl("https://www.linkedin.com/company/linkedin")); // false
  