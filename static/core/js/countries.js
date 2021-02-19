const selectCountry = document.querySelector('#inputCountry');
const selectState = document.querySelector('#inputState');
const flag = document.querySelector('#flag');
const mobile_number = document.querySelector('#inputPhoneNo');
const flagImage = document.createElement('img');
let countries;
let states;
const xhrCountry = new XMLHttpRequest();
xhrCountry.onreadystatechange = () => {
    // console.log(xhrCountry.status);
    if (xhrCountry.readyState === 4 && xhrCountry.status === 200) {
        countries = JSON.parse(xhrCountry.responseText);
        countries.forEach(country => {
            var selectOptions = document.createElement('option');
            selectOptions.value = country['name'];
            selectOptions.textContent = country['name'];
            selectCountry.appendChild(selectOptions);
            console.log(country['name'])
        });
    }
}
xhrCountry.open('POST', './js/countries.json', true);
xhrCountry.send();
const action = () => {
    selectState.innerHTML = '';
    let selectedCountry = selectCountry.value;
    let selectedCountryJSON = countries.find(country => selectedCountry === country['name']);
    // console.log(mobile_number);
    mobile_number.setAttribute('placeholder', '+' + selectedCountryJSON['callingCodes'][0]);
    flagImage.src = selectedCountryJSON['flag'];
    flagImage.width = 50;
    flagImage.height = 25;
    flagImage.alt = selectedCountryJSON['alpha3Code'];
    // console.log(flagImage);
    flag.appendChild(flagImage);
    let countryStates;
    let xhrState = new XMLHttpRequest();
    xhrState.onreadystatechange = () => {
        if (xhrState.readyState === 4 && xhrState.status === 200) {
            try {
                let statesJSON = JSON.parse(xhrState.responseText);
                countryStates = statesJSON.find(state => selectedCountry === state['country']);
                states = countryStates['states'];
                states.sort().map(state => {
                    var selectOptions = document.createElement('option');
                    selectOptions.value = state;
                    selectOptions.textContent = state;
                    selectState.appendChild(selectOptions);
                });
            } catch (error) {
                console.error('could not load states at this moment');
            };
        }
    }
    xhrState.open('POST', './js/states.json', true);
    xhrState.send();
}
selectCountry.addEventListener('change', action);