function calculate() {
    var fo2 = parseFloat(document.getElementById("mix-fo2").value);
    var startPsi = parseFloat(document.getElementById("start-pressure").value);
    var endPsi = parseFloat(document.getElementById("end-pressure").value);
    var maxPsi = parseFloat(document.getElementById("max-pressure").value);
    var maxCapacity = parseFloat(document.getElementById("max-capacity").value);

    var psiGasAdded = endPsi - startPsi;
    var psiO2Added = psiGasAdded * fo2;

    var startCuft = getCuftOfGas(startPsi, maxPsi, maxCapacity);
    var cuftGasAdded = getCuftOfGas(endPsi, maxPsi, maxCapacity) - startCuft;
    var cuftO2Added = getCuftOfGas(psiO2Added, maxPsi, maxCapacity);

    document.getElementById("gas-fo2").innerHTML = (fo2 * 100).toFixed(0);
    document.getElementById("gas-psi-added").innerHTML = psiGasAdded.toFixed(0);
    document.getElementById("o2-psi-added").innerHTML = psiO2Added.toFixed(0);
    document.getElementById("gas-cuft-added").innerHTML = cuftGasAdded.toFixed(0);
    document.getElementById("o2-cuft-added").innerHTML = cuftO2Added.toFixed(0);
}

function getCuftOfGas(currentPressure, maxPressure, maxCapacity) {
    return (currentPressure / maxPressure) * maxCapacity;
}

