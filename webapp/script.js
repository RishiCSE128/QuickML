var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
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
  document.getElementById('test').style.display = "block";
}


document.querySelectorAll('.choice').forEach(item => {
  item.addEventListener("click", event => {
      var value = item.value;
      console.log(value);
    })
})

$('#files').parse({
        config: {
            delimiter: ",",
            complete: displayHTMLTable,
        },
        before: function(file, inputElem)
        {
            console.log("Parsing file...", file);
        },
        error: function(err, file)
        {
            console.log("ERROR:", err, file);
        },
        complete: function()
        {
            console.log("Done with all files");
        }
    });

    function displayHTMLTable(results){
    var table = "<table class='table'>";
    var data = results.data;
     
    for(i=0;i<data.length;i++){
        table+= "<tr>";
        var row = data[i];
        var cells = row.join(",").split(",");
         
        for(j=0;j<cells.length;j++){
            table+= "<td>";
            table+= cells[j];
            table+= "</th>";
        }
        table+= "</tr>";
    }
    table+= "</table>";
    $("#parsed_csv_list").html(table);
}