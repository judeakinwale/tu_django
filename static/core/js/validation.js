const validateNames = (_first_name, _last_name, _errorMsg, _name_row) => {
  //names validations
  let isValid = true;
  if (_first_name.value === "" || _last_name.value === "") {
    _errorMsg.id = "errorMsgText";
    _errorMsg.className = "text-danger";
    _errorMsg.textContent = "Name field can not be empty";
    name_row.appendChild(_errorMsg);
    _errorMsg.focus();
    _first_name.focus();
    isValid = false;
  } else if (_first_name.value.length < 3 || _last_name.value.length < 3) {
    _errorMsg.id = "errorMsgText";
    _errorMsg.className = "text-danger";
    _errorMsg.textContent = "Name too short: as to be at least 3 char";
    _name_row.appendChild(_errorMsg);
    _first_name.focus();
    isValid = false;
  }
  return isValid;
};
//validate username
const validateUsername = (_username, _errorMsg) => {
  let isValid = true;
  if (_username.value === "") {
    _errorMsg.id = "errorMsgText";
    _errorMsg.className = "text-danger";
    _errorMsg.textContent = "Username field can not be empty";
    _username.parentNode.insertBefore(_errorMsg, _username.nextSibling);
    _username.focus();
    isValid = false;
  } else if (_username.value.length < 5) {
    _errorMsg.id = "errorMsgText";
    _errorMsg.className = "text-danger";
    _errorMsg.textContent = "Choose at least 5 characters for username";
    _username.parentNode.insertBefore(_errorMsg, _username.nextSibling);
    _username.focus();
    isValid = false;
  }
  return isValid;
};
//validate email
const validateEmail = (_e_mail, _errorMsg) => {
  let isValid = true;
  return isValid;
};
//validate Mobile number
const validateMobileNumber = (_mobile_number, _errorMsg) => {
  let isValid = true;
  if (_mobile_number.value === "") {
    _errorMsg.id = "errorMsgText";
    _errorMsg.className = "text-danger";
    _errorMsg.textContent = "Phone number field can not be empty";
    _mobile_number.parentNode.insertBefore(
      _errorMsg,
      _mobile_number.nextSibling
    );
    _mobile_number.focus();
    isValid = false;
  } else if (!Number(_mobile_number.value)) {
    _errorMsg.id = "errorMsgText";
    _errorMsg.className = "text-danger";
    _errorMsg.textContent = "Not a valid phone number";
    _mobile_number.parentNode.insertBefore(
      _errorMsg,
      _mobile_number.nextSibling
    );
    _mobile_number.focus();
    isValid = false;
  }
  return isValid;
};
//validate DoB
const validateDateOfBirth = (_date_of_birth, _errorMsg) => {
  let isValid = true;
  let dobValue = _date_of_birth.value;
  let yearOfBirth = new Date(dobValue).getFullYear();
  let currentYear = new Date().getFullYear();
  let age = currentYear - yearOfBirth;
  if (dobValue === "") {
    _errorMsg.id = "errorMsgText";
    _errorMsg.className = "text-danger";
    _errorMsg.textContent = "DoB field can not be empty";
    _date_of_birth.parentNode.insertBefore(
      _errorMsg,
      _date_of_birth.nextSibling
    );
    _date_of_birth.focus();
    isValid = false;
  } else if (age < 18) {
    _errorMsg.id = "errorMsgText";
    _errorMsg.className = "text-danger";
    _errorMsg.textContent = "Only user about 18 can register";
    _date_of_birth.parentNode.insertBefore(
      _errorMsg,
      _date_of_birth.nextSibling
    );
    _date_of_birth.focus();
    isValid = false;
  }
  return isValid;
};
//validate password
const validatePassword = (_password, _errorMsg) => {
  let isValid = true;
  if (_password.value === "") {
    _errorMsg.id = "errorMsgText";
    _errorMsg.className = "text-danger";
    _errorMsg.textContent = "password field can not be empty";
    _password.parentNode.insertBefore(_errorMsg, _password.nextSibling);
    _password.focus();
    isValid = false;
  } else if (_password.value.length < 8) {
    _errorMsg.id = "errorMsgText";
    _errorMsg.className = "text-danger";
    _errorMsg.textContent = "password must be at least 8 character";
    _password.parentNode.insertBefore(_errorMsg, _password.nextSibling);
    _password.focus();
    isValid = false;
  } else if (_password.value.length > 20) {
    _errorMsg.id = "errorMsgText";
    _errorMsg.className = "text-danger";
    _errorMsg.textContent = "password must be at most 20 character";
    _password.parentNode.insertBefore(_errorMsg, _password.nextSibling);
    _password.focus();
    isValid = false;
  }
  return isValid;
};
//check if T/C is aknownledged
const validateCheckAgree = (_check_agree, _errorMsg) => {
  let isValid = true;
  if (!_check_agree.checked) {
    _errorMsg.id = "errorMsgText";
    _errorMsg.className = "text-danger";
    _errorMsg.innerHTML =
      "<p>Terms and conditions must be acknownledge before proceding<p>";
    _check_agree.parentNode.appendChild(_errorMsg); //insertBefore(_errorMsg, _check_agree.nextSibling);
    _check_agree.focus();
    isValid = false;
  }
  return isValid;
};
const validateSignUp = () => {
  var first_name = document.querySelector("#InputFirstName");
  var last_name = document.querySelector("#InputLastName");
  var username = document.querySelector("#validationServerUsername");
  var e_mail = document.querySelector("#emailHelp");
  var mobile_number = document.querySelector("#inputPhoneNo");
  var date_of_birth = document.querySelector("#inputDoB");
  var password = document.querySelector("#inputPassword");
  // var country = document.querySelector('#inputCountry');
  // var state = document.querySelector('#inputState');
  // var address = document.querySelector('#inputAddress');
  // var city = document.querySelector('#inputCity');
  var check_agree = document.querySelector("#Check1");
  var name_row = document.querySelector("#name_row");
  var errorMsgText = document.querySelectorAll("#errorMsgText");
  var errorMsg = document.createElement("small");
  //clear all errors
  if (errorMsgText) {
    errorMsgText.forEach(text => text.remove());
  }
  // is validation met;
  let submitForm =
    validateNames(first_name, last_name, errorMsg, name_row) &&
    validateUsername(username, errorMsg) &&
    validateEmail(e_mail, errorMsg) &&
    validateMobileNumber(mobile_number, errorMsg) &&
    validateDateOfBirth(date_of_birth, errorMsg) &&
    validatePassword(password, errorMsg) &&
    validateCheckAgree(check_agree, errorMsg);
  return submitForm;
};
const validateSignIn = () => {
  var e_mail = document.querySelector("#emailHelp");
  var password = document.querySelector("#inputPassword");
  var errorMsgText = document.querySelectorAll("#errorMsgText");
  var errorMsg = document.createElement("small");
  //clear all errors
  if (errorMsgText) {
    errorMsgText.forEach(text => text.remove());
  }
  // is validation met;
  let submitForm =
    validateEmail(e_mail, errorMsg) && validatePassword(password, errorMsg);
  return submitForm;
};
const validateEventName = _element => {
  if (_element.value == "") {
    _element.focus();
    _element.style.border = "1px solid red";
    return false;
  } else if (_element.value.length < 5) {
    _element.focus();
    _element.style.border = "1px solid red";
    return false;
  } else {
    _element.style.border = "1px solid green";
    return true;
  }
};
const validateDescription = _element => {
  if (_element.value == "") {
    _element.focus();
    _element.style.border = "1px solid red";
    return false;
  } else if (_element.value.length < 5) {
    _element.focus();
    _element.style.border = "1px solid red";
    return false;
  } else {
    _element.style.border = "1px solid green";
    return true;
  }
};
// const validateDescription = _element => {
//   if (_element.value == "") {
//     _element.focus();
//     _element.style.border = "1px solid red";
//     return false;
//   } else if (_element.value.length < 10) {
//     _element.focus();
//     _element.style.border = "1px solid red";
//     return false;
//   } else {
//     _element.style.border = "1px solid green";
//     return true;
//   }
// };
const validateCreateEvent = () => {
  const event_name = document.querySelector("#eventName");
  const description = document.querySelector("#description");
  const image_upload = document.querySelector("#imageUpload");
  const image_upload_name = document.querySelector("#imageUpload-name");
  const location = document.querySelector("#location");
  const city = document.querySelector("#city");
  const country = document.querySelector("#country");
  const state = document.querySelector("#state");
  const ticket_price = document.querySelector("#ticketPrice");
  const ticket_limit = document.querySelector("#ticketLimit");
  const category = document.querySelector("#category");
  const event_package = document.querySelector("#eventPackage");

  // image_upload.addEventListener("change", validateImage(image_upload));

  //   validateNames(event_name, description);
  return (
    validateEventName(event_name) &&
    validateDescription(description) &&
    validateEventName(location) &&
    validateEventName(city)

    // validateImage(image_upload)
  );
};
