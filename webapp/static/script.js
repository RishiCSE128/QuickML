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

function makeVarMap1() {
  const radioButtons = document.querySelectorAll('.rd');
  for (const x of radioButtons) {
    if (x.checked) {
      console.log(x.value)
      console.log('True')
    }
    else {
      console.log(x.value)
      console.log('False')
    }
  }
}



//document.getElementById("someId").getElementsByClassName("someClass")[0].getElementsByTagName("div")[0]



