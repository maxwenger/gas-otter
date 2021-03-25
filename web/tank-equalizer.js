function calculate() {
    var fo21 = parseFloat(document.getElementById("input-fo2-1").value);
    var fo22 = parseFloat(document.getElementById("input-fo2-2").value);
    var maxpsi1 = parseFloat(document.getElementById("input-pressure-1").value);
    var maxpsi2 = parseFloat(document.getElementById("input-pressure-2").value);
    var currentpsi1 = parseFloat(document.getElementById("input-current-pressure-1").value);
    var currentpsi2 = parseFloat(document.getElementById("input-current-pressure-2").value);
    var maxcapacity1 = parseFloat(document.getElementById("input-volume-1").value);
    var maxcapacity2 = parseFloat(document.getElementById("input-volume-2").value);

    var volume1 = getVolume(maxpsi1, maxcapacity1);
    var volume2 = getVolume(maxpsi2, maxcapacity2);
    
    var newPressure = getEqualizationPressure(currentpsi1, volume1, currentpsi2, volume2);

    document.getElementById("new-pressure-1").innerHTML = newPressure.toFixed(0);
    document.getElementById("new-pressure-2").innerHTML = newPressure.toFixed(0);

    var newFo21 = getNewFo2(fo21, currentpsi1, fo22, (newPressure - currentpsi1)); 
    var newFo22 = getNewFo2(fo22, currentpsi2, fo21, (newPressure - currentpsi2)); 

    document.getElementById("new-fo2-1").innerHTML = newFo21.toFixed(2);
    document.getElementById("new-fo2-2").innerHTML = newFo22.toFixed(2);
}

function getNewFo2(currentFo2, currentPressure, addedFo2, addedPressure) {

    if(addedPressure <= 0) {
        console.log(currentFo2);
        return currentFo2;
    }

    var o2Psis = currentFo2 * currentPressure;
    o2Psis += addedFo2 * addedPressure;

    return o2Psis / (currentPressure + addedPressure);
}

function getVolume(pressure, capacity) {
    var psisPerAta = 14.7;

    return (capacity * psisPerAta) / pressure;
}

function getEqualizationPressure(pressure1, volume1, pressure2, volume2) {
    var pressureAvg = pressure1 * volume1;
    pressureAvg += pressure2 * volume2;
    pressureAvg /= (volume1 + volume2);

    return pressureAvg;
}
