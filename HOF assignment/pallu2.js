function generateRandomNumberWithDelay(delayTimeInMilliseconds, progressCallback, completionCallback) {
  // Set a total duration for the delay
  const totalDelayTime = 5000;
  let elapsedDelayTime = 0;

  // Use setInterval to create a delay that progresses over time
  const delayInterval = setInterval(() => {
    elapsedDelayTime += delayTimeInMilliseconds;
    const progress = Math.floor((elapsedDelayTime / totalDelayTime) * 100);
    progressCallback(progress);

    if (elapsedDelayTime >= totalDelayTime) {
      // Once the delay is complete, generate a random number and call the completion callback
      clearInterval(delayInterval);
      const randomNumber = Math.floor(Math.random() * 100) + 1;
      completionCallback(randomNumber);
    }
  }, delayTimeInMilliseconds);
}
