
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function () {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}

function showDiv() {
  document.getElementById('appear1').style.display = "block";
}

document.querySelectorAll('.choice').forEach(item => {
  item.addEventListener("click", event => {
    var value = item.value;
    console.log(value);
  })
})

function isChecked(x) {
  const radioButtons = document.querySelectorAll('.rd');

  for (const radioButton of radioButtons) {
    if (x.checked) {

      console.log(x.value)
    }
    else {
      console.log(x.value)
    }
  }
}


function makeVarMap() {

  const radioButtons = document.querySelectorAll('.rd');  // All radio buttons
  const headers = document.querySelectorAll('th.rt');     // Headers

  var varMap = {
    'Independent': [],
    'Dependent': [],
    'Categorical': []
  }

  var head = [];
  for (let i = 0; i < headers.length; ++i) {
    head[i] = headers[i].textContent;
  }
  var j = 0;
  for (let x = 0; x < radioButtons.length; x++) {
    if (radioButtons[x].checked && radioButtons[x].value == 'Ind') {
      varMap['Independent'].push(head[j]);
      j++;
    }
    if (radioButtons[x].checked && radioButtons[x].value == 'Dep') {
      varMap['Dependent'].push(head[j]);
      j++;
    }
    if (radioButtons[x].checked && radioButtons[x].value == 'Cat') {
      j--;
      varMap['Categorical'].push(head[j]);
      j++;
    }
  }
  console.log(varMap);
}

$(document).ready(function () {
  $('input.dep:radio').change(function() {
      // When any radio button on the page is selected,
      // then deselect all other radio buttons.
      $('input.dep:radio:checked').not(this).prop('checked', false);
  });
})