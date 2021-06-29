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


// // For resizing event images uploaded (doesn't work)
// $(document).ready(function () {

//   $('#id_image').change(function (evt) {

//     var files = evt.target.files;
//     var file = files[0];

//     if (file) {
//       var reader = new FileReader();
//       reader.onload = function (e) {
//         document.getElementById('preview').src = e.target.result;
//       };
//       reader.readAsDataURL(file);
//     }
//   });
// });

// function ResizeImage() {
//   if (window.File && window.FileReader && window.FileList && window.Blob) {
//     var filesToUploads = document.getElementById('id_image').files;
//     var file = filesToUploads[0];
//     if (file) {

//       var reader = new FileReader();
//       // Set the image once loaded into file reader
//       reader.onload = function (e) {

//         var img = document.createElement("img");
//         img.src = e.target.result;

//         var canvas = document.createElement("canvas");
//         var ctx = canvas.getContext("2d");
//         ctx.drawImage(img, 0, 0);

//         var MAX_WIDTH = 400;
//         var MAX_HEIGHT = 400;
//         var width = img.width;
//         var height = img.height;

//         if (width > height) {
//           if (width > MAX_WIDTH) {
//             height *= MAX_WIDTH / width;
//             width = MAX_WIDTH;
//           }
//         } else {
//           if (height > MAX_HEIGHT) {
//             width *= MAX_HEIGHT / height;
//             height = MAX_HEIGHT;
//           }
//         }
//         canvas.width = width;
//         canvas.height = height;
//         var ctx = canvas.getContext("2d");
//         ctx.drawImage(img, 0, 0, width, height);

//         dataurl = canvas.toDataURL(file.type);
//         document.getElementById('output').src = dataurl;
//       }
//       reader.readAsDataURL(file);

//     }

//   } else {
//     alert('The File APIs are not fully supported in this browser.');
//   }
// }