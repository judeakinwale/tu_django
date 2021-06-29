function showpass() {
  var pswd = document.getElementById("inputPassword");
  var showhide = document.getElementById("show-eye");
  if (pswd.type === "password") {
    pswd.type = "text";
    showhide.className = "fa fa-eye";
  } else {
    pswd.type = "password";
    showhide.className = "fa fa-eye-slash";
  }
}
// const single_event_link = document.querySelectorAll(".single-event-link");
// const show_single_event = () => {
//     const fetch_single_event = new XMLHttpRequest();
//     fetch_single_event.open('POST','./connections/single_event_process.php');
//     fetch_single_event.send();
// };
// single_event_link.forEach(anchor =>
//   anchor.addEventListener("click", show_single_event)
// );
