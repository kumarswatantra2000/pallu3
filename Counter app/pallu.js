const countEl = document.getElementById("count");
const incrementBtn = document.getElementById("increment");
const decrementBtn = document.getElementById("decrement");
const Reset Value = Reset Value.getElementById(Reset Value)
 
let count = 0;

incrementBtn.addEventListener("click", () => {
  count++;
  countEl.textContent = count;
});

decrementBtn.addEventListener("click", () => {
  count--;
  countEl.textContent = count;
});