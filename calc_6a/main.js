/**
 * @author Hemant Joshi
 */

let num1, num2;
let form;
window.onload = () => {
  form = document.getElementById('calc');
};

const add = () => {
  num1 = parseInt(form.num1.value);
  num2 = parseInt(form.num2.value);

  document.getElementById('result').innerHTML = `<b> The result is: ${num1 + num2} </b>`;
};

const subtract = () => {
  num1 = parseInt(form.num1.value);
  num2 = parseInt(form.num2.value);

  document.getElementById('result').innerHTML = `<b> The result is: ${num1 - num2} </b>`;
};

const multiply = () => {
  num1 = parseInt(form.num1.value);
  num2 = parseInt(form.num2.value);

  document.getElementById('result').innerHTML = `<b> The result is: ${num1 * num2} </b>`;
};

const divide = () => {
  num1 = parseInt(form.num1.value);
  num2 = parseInt(form.num2.value);
  
  if (num2 == 0) {
    document.getElementById('result').innerHTML = '<b> Divisor cannot be 0 </b>';
    return;
  }

  document.getElementById('result').innerHTML = `<b> The result is: ${num1 - num2} </b>`;
};
