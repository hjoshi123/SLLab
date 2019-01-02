function validateForm(button) {
  const form = document.getElementById('atm');

  if (form.amount.value == '') {
    alert ('Amount required');
    return false;
  }

  if (parseInt(form.amount.value) < 0) {
    alert ('Cannot enter negative value');
    return false;
  }

  if (button.value == 'Withdraw' && parseInt(form.amount.value) > 5000) {
    console.log('Entered here');
    alert ('Cannot withdraw more than 5000');
    return false;
  }

  return true;
}