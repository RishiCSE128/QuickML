
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
  document.getElementById('appear0').style.display = "block";
}

document.querySelectorAll('.choice').forEach(item => {
  item.addEventListener("click", event => {
    var value = item.value;
    console.log(value);

    let option = value
    console.log(option)
    const request = new XMLHttpRequest()
    request.open('POST', `/ProcessOption/${JSON.stringify(option)}`)
    request.send();
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


$('.choice').click(function () {
  $('#appear1').toggle('slow', function () {

  });
});

function makeDNN_Arch(){
  // Obtaining relevant data from the DOM
  const options = document.querySelectorAll('.selected');  // All user choices
  const headers = document.querySelectorAll('th');   // All headers

  // Creating blank dictionary to be populated
  var Dnn_Arch = {
    'Layers' : [],
    'Optimization Function': [],
    'Loss Function': [],
    'Batch Size': [],
    'Epoch': []
  }

  

}


// Makes the variable mapping to be passed into data pre-processing function
function makeVarMap() {

  const radioButtons = document.querySelectorAll('.rd');  // All radio buttons
  const headers = document.querySelectorAll('th.rt');     // Headers

  var varMap = {
    'Independent': [],
    'Dependent': [],
    'Categorical': [],
    'Ignored': []
  }

  var head = [];
  for (let i = 0; i < headers.length; ++i) {
    // index i tracks row by row 
    head[i] = headers[i].textContent;
  }
  // Seperate index to track column - name of attribute 
  var j = 0;
  for (let x = 0; x < radioButtons.length; x++) {
    if (radioButtons[x].checked && radioButtons[x].value == 'Ind') {
      varMap['Independent'].push(head[j]);
      j++;
      // Adds into respective category and increments the COLUMN index 
    }
    if (radioButtons[x].checked && radioButtons[x].value == 'Dep') {
      varMap['Dependent'].push(head[j]);
      j++;
    }
    if (radioButtons[x].checked && radioButtons[x].value == 'Ignore') {
      varMap['Ignored'].push(head[j]);
      j++;
    }
    if (radioButtons[x].checked && radioButtons[x].value == 'Cat') {
      j--;  // Categorical is always also dependent or independent
      varMap['Categorical'].push(head[j]);
      j++; // decrements j before the logic, so it targets the correct block
    }
  }
  s = JSON.stringify(varMap)
  // Convert to JSON so it can be send
  // Sent with asonchronous javascript 
  $.ajax({
    url: '/dataPreProcessing',
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify(s)
  }).done(function (result) {     // When function returns append data to div in DOM
    var div = document.createElement("div");
    // Creating DIV and appending to existing div in DOM 
    div.style.width = "100%";
    div.style.background = "#007bff80";
    div.innerHTML = result;
    div.style.margin = "auto";

    document.getElementById("main").appendChild(div);
    document.getElementById('Xar').style.display = "block";
    // Make other data visible 
  })
}

// Radio button logic done in JQuery
$(document).ready(function () {
  $('input.dep:radio').change(function () {
    // When any radio button on the page is selected,
    // then deselect all other radio buttons.
    $('input.dep:radio:checked').not(this).prop('checked', false);
  });
})