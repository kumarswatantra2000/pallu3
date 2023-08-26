function generateRandomNumberWithDelay(delayTimeInMilliseconds, progressCallback, completionCallback) {
    const totalDelayTime = 5000; // Set a total duration for the delay
    let elapsedDelayTime = 0;
  
    const delayInterval = setInterval(() => {
      elapsedDelayTime += delayTimeInMilliseconds;
      const progress = Math.floor((elapsedDelayTime / totalDelayTime) * 100);
      progressCallback(progress);
  
      if (elapsedDelayTime >= totalDelayTime) {
        clearInterval(delayInterval); // Once the delay is complete, stop the interval
        const randomNumber = Math.floor(Math.random() * 100) + 1; // Generate a random number
        completionCallback(randomNumber); // Call the completion callback with the random number
      }
    }, delayTimeInMilliseconds);
  }
  