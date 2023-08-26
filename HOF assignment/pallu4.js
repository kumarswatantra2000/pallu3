// Example array of books
const books = [
    { title: "book 1", author: "author 1", year: 2009 },
    { title: "book 2", author: "author 2", year: 2015 },
    { title: "book 3", author: "author 3", year: 2012 },
    { title: "book 4", author: "author 4", year: 2018 }
  ];
  
  // Filter and capitalize book titles published after 2010 with author names
  const filteredBooks = books.filter(book => book.year > 2010).map(book => {
    return {
      title: book.title.toUpperCase(),
      author: book.author.toUpperCase()
    };
  });
  
  // Output the filtered books
  console.log(filteredBooks);
  