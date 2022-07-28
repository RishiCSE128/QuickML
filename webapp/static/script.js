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

function makeVarMap1() {
  var tbl = $('table#data tr').map(function() {
    return $(this).find('td').map(function() {
      return $(this).text();
    }).get();
  }).get();
  console.log(tbl)
}



//document.getElementById("someId").getElementsByClassName("someClass")[0].getElementsByTagName("div")[0]



// function makeVarMap() {
//   [...document.getElementsByClassName(".dynamic")].forEach(item => {
//     var key = $("input[type='radio']:checked").val();
//     console.log(key)
//   })
// }