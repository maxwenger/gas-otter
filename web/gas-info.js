var OXY_DENSITY = 1.43;
var NITROGEN_DENSITY = 1.25;

function refreshGasInfo() {
    var fo2 = parseFloat(document.getElementById("inputFo2").value);
    var surfacePressure = parseFloat(document.getElementById("inputSurfPressure").value);
    var pressureDepthConversionFactor = getPressureDepthConversionFactor();

    var table = document.getElementById("gas-info-table").getElementsByTagName("tbody")[0];

    while(table.firstChild) {
        table.removeChild(table.firstChild);
    }
    

    var i;
    for(i = 0; i <= 300; i += 10) {
        let depth = i;
        let pressure = getHydrostaticPressure(i, pressureDepthConversionFactor) + surfacePressure;
        let ppo2 = getPartialPressure(fo2, pressure);
        let ppn2 = getPartialPressure(1 - fo2, pressure);
        let gasDensity = getDensityComponent(ppo2, OXY_DENSITY);
        gasDensity += getDensityComponent(ppn2, NITROGEN_DENSITY);

        addRow(table, depth, pressure, ppo2, ppn2, gasDensity);
    }
}

// Will return the depth required to equal one atmosphere of pressure given
// the density of water. So, for fresh water, it will return 34 ft.
function getPressureDepthConversionFactor() {
    var radio = document.getElementsByName('water-density-radio');

    for(i in radio) {
        if(radio[i].checked) {
            let name = radio[i].value;
            
            if(name == "salt") {
                return 33;
            } else if(name == "fresh") {
                return 34;
            } else {
                return 0;
            }
        }
    }

}

function addRow(table, depth, pressure, ppo2, ppn2, gasDensity) {
    let row = table.insertRow();
    
    pressure = pressure.toFixed(2);
    ppo2 = ppo2.toFixed(2);
    ppn2 = ppn2.toFixed(2);
    gasDensity = gasDensity.toFixed(2);

    if(isGasDanger(ppo2,gasDensity)) {
        row.setAttribute('class', 'table-danger');
    } else if(isGasWarn(ppo2, gasDensity)) {
        row.setAttribute('class', 'table-warning');
    }

    let depthText = document.createTextNode(depth);
    let pressureText = document.createTextNode(pressure);
    let ppo2Text = document.createTextNode(ppo2);
    let ppn2Text = document.createTextNode(ppn2);
    let gasDensityText = document.createTextNode(gasDensity);

    row.insertCell().appendChild(depthText);
    row.insertCell().appendChild(pressureText);
    row.insertCell().appendChild(ppo2Text);
    row.insertCell().appendChild(ppn2Text);
    row.insertCell().appendChild(gasDensityText);
}

function isGasWarn(ppo2, gasDensity) {
    return isPPO2Warn(ppo2) || isGasDensityWarn(gasDensity);
}

function isGasDanger(ppo2, gasDensity) {
    return isPPO2Danger(ppo2);
}

function isPPO2Warn(ppo2) {
    return ppo2 >= 1.4;
}

function isPPO2Danger(ppo2) {
    return 0.16 >= ppo2 || ppo2 >= 1.6;
}

function isGasDensityWarn(gasDensity) {
    return gasDensity >= 6;
}

function getPartialPressure(fog, pressure) {
    return fog * pressure;
}

function getDensityComponent(ppog, density) {
    return ppog * density;
}

function getHydrostaticPressure(depth, pressureDepthConversionFactor) {
    return depth / pressureDepthConversionFactor;
}

function getModFt(fo2, maxPpo2, pressureDepthConversionFactor) {
    var mod = maxPpo2 / fo2;
    mod -= 1;
    mod = mod * pressureDepthConversionFactor;
    return mod;
}

function init() {
    refreshGasInfo();
    document.getElementById('submit-gas-info').onclick = refreshGasInfo;
}

window.onload = init;
