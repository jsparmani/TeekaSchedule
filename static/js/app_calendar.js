var dt = new Date();
function renderDate() {
  //  dt.setDate(1);

  var day = dt.getDay();
  var firstDate = new Date(dt.getFullYear(), dt.getMonth(), 1);
  firstDay = firstDate.getDay();
  console.log(firstDay);
  var endDate = new Date(dt.getFullYear(), dt.getMonth() + 1, 0).getDate();

  var prevDate = new Date(dt.getFullYear(), dt.getMonth(), 0).getDate();

  var today = new Date();
  var months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
  ];

  document.getElementById("date_str").innerHTML = dt.toDateString();
  document.getElementById("month").innerHTML = months[dt.getMonth()];

  var grids = "";
  for (x = firstDay; x > 0; x--) {
    grids += "<div class ='prev_date' >" + (prevDate - x + 1) + "</div>";
  }
  for (i = 1; i <= endDate; i++) {
    if (i == today.getDate() && dt.getMonth() == today.getMonth()) {
      grids += "<div class= 'today'>" + i + "</div>";
    } else {
      grids += "<div>" + i + "</div>";
    }
  }
  console.log(document.getElementsByClassName("days")[0]);
  document.getElementsByClassName("days")[0].innerHTML = grids;
}
function moveDate(para) {
  if (para == "prev") {
    dt.setMonth(dt.getMonth() - 1);
    console.log("hello")
  } else if (para == "next") {
    dt.setMonth(dt.getMonth() + 1);
  }
  renderDate();
}

console.log(dt.getMonth());
console.log(dt.setMonth(dt.getMonth()));
